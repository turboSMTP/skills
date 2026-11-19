"""Verify the catalog, local references, evaluation IDs and distributed bytes."""
import hashlib
import json
import re
from pathlib import Path
from zipfile import ZipFile

from package import ROOT


def check(output):
    documents = {entry.parent.name: entry for entry in (ROOT / "skills").glob("*/SKILL.md")}
    catalog = (ROOT / "docs/CATALOG.md").read_text()
    expected = set(re.findall(r"^## \d+\. (turbosmtp-[a-z-]+)$", catalog, re.M))
    assert documents.keys() == expected, "installed catalog differs from the specification"
    cases = json.loads((ROOT / "evals/cases.json").read_text())
    assert len({item["id"] for item in cases}) == len(cases)
    combined = set()
    with ZipFile(output / "turbosmtp-skills.zip") as bundle:
        for name, entry in documents.items():
            content = entry.read_text()
            assert content.startswith(f"---\nname: {name}\ndescription: >-\n  ")
            assert sum(item["skill"] == name for item in cases) == 6, name
            with ZipFile(output / f"{name}.zip") as single:
                files = {p for p in entry.parent.rglob("*") if p.is_file()}
                paths = {f"{name}/{p.relative_to(entry.parent)}": p for p in files}
                paths[f"{name}/LICENSE"] = ROOT / "LICENSE"
                assert set(single.namelist()) == paths.keys()
                for relative, source in paths.items():
                    assert single.read(relative) == bundle.read(relative) == source.read_bytes()
                    if source.suffix == ".md":
                        for target in re.findall(r"\]\(([^)]+)\)", source.read_text()):
                            if not target.startswith(("https://", "#")):
                                linked = (source.parent / target.split("#")[0]).resolve()
                                assert linked.is_relative_to(entry.parent) and linked.is_file(), target
                combined.update(paths)
        assert combined == set(bundle.namelist())
    for line in (output / "SHA256SUMS").read_text().splitlines():
        digest, name = line.split("  ")
        assert hashlib.sha256((output / name).read_bytes()).hexdigest() == digest


if __name__ == "__main__":
    import sys
    check(Path(sys.argv[1]))
