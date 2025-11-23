#!/usr/bin/env python3
"""Cleanup script for removing stale documentation preview builds.

This script removes preview build directories for pull requests that have been
closed or no longer exist. It's designed to run periodically via GitHub Actions
to keep the preview repository clean.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from shutil import rmtree

from github import Github


def main() -> None:
    """Remove preview build directories for closed or non-existent PRs."""
    parser = argparse.ArgumentParser(
        description="Remove stale PR preview builds from gh-pages branch"
    )
    parser.add_argument("gh_token", help="GitHub authentication token")
    parser.add_argument("repository", help="Repository name (owner/repo)")
    args = parser.parse_args()

    # Initialize GitHub client
    gh = Github(args.gh_token)
    repo = gh.get_repo(args.repository)

    # Checkout gh-pages branch
    subprocess.run(["git", "checkout", "gh-pages"], check=True)

    # Track if any changes were made
    deleted_any = False

    # Scan for numbered preview directories
    for path in Path(".").iterdir():
        if not path.is_dir() or not path.name.isdigit():
            continue

        pr_number = int(path.name)

        try:
            # Check if PR exists and is open
            pr = repo.get_pull(pr_number)
            if pr.state == "closed":
                print(f"Removing preview for closed PR #{pr_number}")
                rmtree(path)
                deleted_any = True
        except Exception:
            # PR doesn't exist
            print(f"Removing preview for non-existent PR #{pr_number}")
            rmtree(path)
            deleted_any = True

    # Commit and push if changes were made
    if deleted_any:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(
            ["git", "commit", "-m", "chore: remove stale preview builds"],
            check=True,
        )
        subprocess.run(["git", "push"], check=True)
        print("Stale preview builds removed and changes pushed")
    else:
        print("No stale preview builds found")

    # Return to original branch
    subprocess.run(["git", "checkout", "-"], check=True)


if __name__ == "__main__":
    main()
