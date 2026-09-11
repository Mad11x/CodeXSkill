#!/usr/bin/env python3
"""Collect one author's committed changes from all local branches and repositories."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path


DEFAULT_ROOT = Path("/Users/mad/workspace")
DEFAULT_AUTHOR = "madma"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Collect commits and patches from every Git repository beneath a root. "
            "Only commits reachable from local branches are included."
        )
    )
    parser.add_argument(
        "--date",
        dest="report_date",
        type=date.fromisoformat,
        default=datetime.now().astimezone().date(),
        help="Report date in YYYY-MM-DD form; defaults to today.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help=f"Repository search root; defaults to {DEFAULT_ROOT}.",
    )
    parser.add_argument(
        "--author",
        default=DEFAULT_AUTHOR,
        help=f"Case-insensitive author name/email pattern; defaults to {DEFAULT_AUTHOR}.",
    )
    return parser.parse_args()


def discover_repositories(root: Path) -> list[Path]:
    repositories: list[Path] = []
    for current, directories, files in os.walk(root):
        if ".git" in directories or ".git" in files:
            repositories.append(Path(current))
            if ".git" in directories:
                directories.remove(".git")
    return sorted(set(repositories))


def git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def commit_hashes(repo: Path, report_date: date, author: str) -> list[str]:
    start = f"{report_date.isoformat()} 00:00:00"
    end = f"{report_date.isoformat()} 23:59:59"
    result = git(
        repo,
        "log",
        "--branches",
        "--regexp-ignore-case",
        f"--author={author}",
        f"--since={start}",
        f"--until={end}",
        "--reverse",
        "--format=%H",
    )
    if result.returncode != 0:
        print(f"WARNING: unable to read {repo}: {result.stderr.strip()}", file=sys.stderr)
        return []
    return list(dict.fromkeys(line for line in result.stdout.splitlines() if line))


def render_commit(repo: Path, commit_hash: str) -> str:
    result = git(
        repo,
        "show",
        "--no-ext-diff",
        "--find-renames",
        "--stat",
        "--patch",
        "--unified=3",
        "--format=COMMIT %H%nAUTHOR %an <%ae>%nDATE %aI%nSUBJECT %s%nBODY %b",
        commit_hash,
    )
    if result.returncode != 0:
        return f"WARNING: unable to inspect {commit_hash}: {result.stderr.strip()}"
    return result.stdout.rstrip()


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: repository root does not exist: {root}", file=sys.stderr)
        return 2

    matches = 0
    for repo in discover_repositories(root):
        hashes = commit_hashes(repo, args.report_date, args.author)
        if not hashes:
            continue
        relative = repo.relative_to(root)
        print(f"\n=== REPOSITORY {relative} ({repo}) ===")
        for commit_hash in hashes:
            matches += 1
            print()
            print(render_commit(repo, commit_hash))

    if matches == 0:
        print(
            f"NO_MATCHING_COMMITS date={args.report_date.isoformat()} "
            f"author={args.author} root={root}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
