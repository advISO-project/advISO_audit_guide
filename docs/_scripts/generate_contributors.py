"""Generate pages/contributors.md from contributors.yml."""

import os
from pathlib import Path

import yaml


def _render_grid(people):
    lines = ["::::{grid} 3", ":gutter: 3", ""]
    for person in people:
        gh = person["github"]
        lines += [
            ":::{grid-item-card}",
            f":img-top: https://github.com/{gh}.png",
            f":link: https://github.com/{gh}",
            "",
            f"**{person['name']}**",
            ":::",
            "",
        ]
    lines.append("::::")
    return "\n".join(lines)


def generate_contributors(github_repo):
    docs_dir = Path(os.path.dirname(__file__)).parent
    config_path = docs_dir / "contributors.yml"
    out_path = docs_dir / "pages" / "contributors.md"

    with open(config_path) as f:
        config = yaml.safe_load(f)

    sections = []
    sections.append("# Contributors\n")

    if config.get("intro"):
        sections.append(config["intro"].strip() + "\n")

    if config.get("authors"):
        sections.append("## Author(s)\n")
        sections.append(_render_grid(config["authors"]))

    if config.get("maintainers"):
        sections.append("\n## Maintainers\n")
        sections.append(_render_grid(config["maintainers"]))

    if config.get("contributors"):
        sections.append("\n## Contributors\n")
        sections.append(_render_grid(config["contributors"]))

    sections.append("\n---\n")
    sections.append(
        f"Want to contribute? Visit our [GitHub repository]({github_repo}) to get involved.\n"
    )

    with open(out_path, "w") as f:
        f.write("\n".join(sections))
