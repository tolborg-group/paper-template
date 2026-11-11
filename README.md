# Tolborg Group — Paper Template

[![Build PDF](https://github.com/tolborg-group/paper-template/actions/workflows/build.yml/badge.svg)](https://github.com/tolborg-group/paper-template/actions/workflows/build.yml)

A LaTeX template for journal articles, with local builds via [Pixi](https://pixi.sh)
and automatic PDF compilation on every commit via GitHub Actions.

## Quickstart

```sh
# clone and enter
git clone <this-repo> my-paper && cd my-paper

# build once (downloads LaTeX packages automatically on first run)
pixi run -e latex build

# rebuild on every save
pixi run -e latex watch
```

The compiled `main.pdf` appears in the root directory.

To download the latest PDF built by CI without cloning:

```sh
gh run download --name paper
```

## Claude Code skills

The template declares the group's [Claude Code](https://claude.com/claude-code)
plugins from [group-skills](https://github.com/tolborg-group/group-skills) in
`.claude/settings.json`. Install them once:

```sh
pixi run setup-claude
```

Then start a skill directly from the terminal:

```sh
pixi run sync       # commit, pull and push, with each git command explained
pixi run diagnose   # find out why main.tex does not compile, and fix it
```

## Repository layout

```
main.tex            – top-level file: preamble, author list, section inputs
sections/           – one file per section (easier diffs, easier co-authoring)
figures/            – source files for all figures (PDF or PNG preferred)
references.bib      – BibTeX database
pixi.toml           – reproducible environment + task aliases
.claude/            – Claude Code settings: group plugins and git safety rules
.github/workflows/  – CI pipeline
```

## Adapting to a target journal

`main.tex` uses [REVTeX 4-2](https://journals.aps.org/revtex) with the `prl`
(Physical Review Letters) class option. To switch journal:

- **Other APS journals** (PRB, PRM, …): change `prl` to `prb`, `prmaterials`, etc.
- **ACS journals**: swap `revtex4-2` for `achemso`; check the
  [achemso docs](https://ctan.org/pkg/achemso) for the `journal` key.
- **Springer/Nature journals**: most supply their own `.cls` file —
  drop it in the root and update `\documentclass` accordingly.

## CI

Every push and pull request triggers a build. The compiled PDF is attached
as a **downloadable artifact** for 30 days — useful for reviewers who want
to read the current state without cloning.

When you are ready to archive a submitted or published version, push a tag:

```sh
git tag v1.0-submitted
git push origin v1.0-submitted
```

This triggers a GitHub Release with the PDF attached.

## Writing conventions

- `\todo{…}` renders in red — search for these before submission.
- `\note{…}` renders in blue — for margin comments between authors.
- Use `\qty{3.5}{\angstrom}` (siunitx) for all physical quantities.
- Use `\cref{…}` (cleveref) rather than `Fig.~\ref{…}` — it adds the label
  type automatically and handles plural references.
- Prefer `\cite` after punctuation in APS style: `result.~\cite{…}`

## Figures

The `figures/` directory holds both the PNG files (committed, used directly by LaTeX) and the Python scripts that generate them. The PNG is the source of truth for the build — the script is provenance that makes it easy to tweak and regenerate.

To regenerate a figure, run its script through the default Python environment:

```sh
pixi run python figures/kpoint-convergence.py
```

### Adding a Python package

```sh
pixi add --pypi <package>
```

For packages that require non-Python system libraries (compiled extensions, binary tools), try conda-forge instead:

```sh
pixi add <package>
```

Commit the updated `pixi.toml` and `pixi.lock` afterwards so collaborators get the same environment.
