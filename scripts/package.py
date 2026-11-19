"""Build reproducible skill archives. Run in a private or public checkout."""
import argparse
import hashlib
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]


def archive(path, members):
    with ZipFile(path, "w") as bundle:
        for name, source in sorted(members):
            info = ZipInfo(name)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, source.read_bytes(), compress_type=ZIP_DEFLATED)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    output = parser.parse_args().output
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        parser.error("choose an empty output directory")
    members = []
    for entry in sorted((ROOT / "skills").glob("*/SKILL.md")):
        directory = entry.parent
        files = [entry, *sorted((directory / "references").glob("*.md"))]
        skill = [(f"{directory.name}/{file.relative_to(directory)}", file) for file in files]
        skill.append((f"{directory.name}/LICENSE", ROOT / "LICENSE"))
        archive(output / f"{directory.name}.zip", skill)
        members.extend(skill)
    if not members:
        raise ValueError("no skills found")
    archive(output / "turbosmtp-skills.zip", members)
    checks = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}" for p in sorted(output.glob("*.zip"))]
    (output / "SHA256SUMS").write_text("\n".join(checks) + "\n")


if __name__ == "__main__":
    main()
