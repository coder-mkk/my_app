
"""Regenerate the workspace LOC summary report."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Iterable

# Exclusions can be expanded if you want to ignore more directories or file types.
EXCLUDE_DIRS = {"__pycache__",
                "fyers_ws_logs",
                "logs",
                "test"
                }
EXCLUDE_SUFFIXES = {".json", ".lock", ".png", ".pyc", ".spec", ".svg", ".toml", ".ui"}


def iter_workspace_files(workspace_root: Path) -> Iterable[Path]:
    """Yield file paths under ``workspace_root`` honoring exclusion rules."""

    for root, dirnames, filenames in os.walk(workspace_root):
        root_path = Path(root)
        rel_root = root_path.relative_to(workspace_root)

        # Drop hidden directories and excluded directory names in-place to prune walk.
        dirnames[:] = [
            d
            for d in dirnames
            if d not in EXCLUDE_DIRS
            and not d.startswith(".")
        ]

        # Skip hidden directory trees outright.
        if any(part.startswith(".") for part in rel_root.parts):
            continue

        for filename in filenames:
            if filename.startswith("."):
                continue
            path = root_path / filename
            if path.suffix in EXCLUDE_SUFFIXES:
                continue
            rel_path = path.relative_to(workspace_root)
            if any(part.startswith(".") for part in rel_path.parts):
                continue
            yield path


def count_lines(path: Path) -> int:
    """Return the number of lines in *path* using UTF-8 with fallback."""
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        return sum(1 for _ in handle)


def main() -> None:
    workspace_root = Path(__file__).resolve().parent.parent
    report_path = workspace_root / "reports" / "workspace_loc_summary.json"

    files_info = []
    directories = set()
    total_loc = 0

    for abs_path in iter_workspace_files(workspace_root):
        rel_path = abs_path.relative_to(workspace_root)
        directories.update(
            str(rel_path.parent) for _ in [None] if rel_path.parent != Path(".")
        )
        loc = count_lines(abs_path)
        total_loc += loc
        files_info.append({"path": rel_path.as_posix(), "loc": loc})

    files_info.sort(key=lambda item: (-item["loc"], item["path"]))

    summary = {
        "exclusions": {
            "directories_named": sorted(EXCLUDE_DIRS),
            "file_suffixes": sorted(EXCLUDE_SUFFIXES),
        },
        "summary": {
            "description": (
                f"Workspace contains {len(files_info)} files across {len(directories)} "
                f"directories with {total_loc} total lines of code."
            ),
            "files": len(files_info),
            "directories": len(directories),
            "total_lines_of_code": total_loc,
        },
        "total_files": len(files_info),
        "total_directories": len(directories),
        "total_loc": total_loc,
        "files": files_info,
    }

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(summary, indent=2))
    print(f"Updated {report_path.relative_to(workspace_root)}")


if __name__ == "__main__":
    main()