# Contributing

Edit the relevant `skills/<name>/SKILL.md` and keep supporting material in its `references/` directory. Make the description specific enough for an agent to select it from a user's request. Link provider-specific behavior to the corresponding turboSMTP documentation.

Add a realistic prompt and observable expected outcome to [the evaluation set](evals/cases.json) when a change affects selection or behavior. Use fictional addresses and fixtures. Include the result of the affected case in your pull request. [Evaluation instructions](evals/README.md)

To reproduce the packaging checks with Python 3.11 or later, choose an empty output directory:

```sh
python3 scripts/package.py dist
python3 scripts/check.py dist
```

The artifacts include a ZIP for each skill, a bundle ZIP and SHA-256 checksums. CI builds and checks the same artifacts on pushes and pull requests. Sign your commits and describe the user task your change improves.
