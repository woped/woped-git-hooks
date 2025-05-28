#!/usr/bin/env python3
import sys
import subprocess
import re


def main():
    # get current branch
    branch = (
        subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
        .decode("utf-8", errors="ignore")
        .strip()
    )

    # exceptions
    if branch in ("main", "master"):
        return 0

    # check pattern
    pattern = r"^(feature)\/[a-z0-9._-]+$"
    if not re.match(pattern, branch):
        sys.stderr.write(f"Invalid branch name: '{branch}'\n")
        sys.stderr.write("Allowed format: feature/short-description\n")
        sys.stderr.write("Example: feature/login-ui\n")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
