#!/usr/bin/env python3
"""Install humanizer skills locally for posts/ workflow.

Clones (or updates) upstream humanizer repos to external/{humanizer-zh,humanizer}/
so that any LLM agent on any machine can run the humanize step end-to-end without
manual setup.

Cross-platform: Python stdlib only (works on Win/macOS/Linux).
Idempotent: re-running pulls instead of failing.
Network-required: git clone + (--refresh-prompts) raw fetch from GitHub.

Usage:
  python tools/install-humanizer.py              # install/update both
  python tools/install-humanizer.py --check      # report status, no changes
  python tools/install-humanizer.py --refresh-prompts  # also re-vendor prompts/

Exit codes:
  0  ok
  1  one or more skills missing/failed (check) or install error (install)
  2  prerequisite missing (no git in PATH)
"""

import argparse
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

# upstream repos: (name, repo_url, vendored_prompt_filename)
REPOS = [
    ("humanizer-zh", "https://github.com/op7418/Humanizer-zh.git", "humanizer-zh.md"),
    ("humanizer",    "https://github.com/blader/humanizer.git",    "humanizer.md"),
]

ROOT = Path(__file__).resolve().parent.parent
EXTERNAL = ROOT / "external"
PROMPTS = ROOT / "prompts"


def have_git() -> bool:
    return shutil.which("git") is not None


def run(cmd, cwd=None) -> int:
    print("  $ " + " ".join(cmd))
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        sys.stderr.write(res.stderr)
    return res.returncode


def install_one(name: str, url: str) -> bool:
    """Clone or update one upstream repo. Returns True on success."""
    dest = EXTERNAL / name
    if (dest / ".git").exists():
        print(f"[{name}] exists at external/{name}/, updating...")
        return run(["git", "-C", str(dest), "pull", "--ff-only"]) == 0
    if dest.exists():
        sys.stderr.write(
            f"[{name}] external/{name}/ exists but is not a git checkout. "
            f"Remove it manually and re-run.\n"
        )
        return False
    print(f"[{name}] cloning to external/{name}/")
    EXTERNAL.mkdir(parents=True, exist_ok=True)
    return run(["git", "clone", "--depth", "1", url, str(dest)]) == 0


def verify_install(name: str) -> bool:
    skill = EXTERNAL / name / "SKILL.md"
    if not skill.exists():
        sys.stderr.write(
            f"[{name}] WARN: external/{name}/SKILL.md missing — "
            f"upstream layout may have changed.\n"
        )
        return False
    return True


def refresh_prompt(name: str, prompt_filename: str) -> bool:
    """Re-fetch SKILL.md from external/<name>/ into prompts/<prompt_filename>,
    preserving the existing attribution header."""
    src = EXTERNAL / name / "SKILL.md"
    dst = PROMPTS / prompt_filename
    if not src.exists():
        sys.stderr.write(f"[{name}] cannot refresh prompt: {src} missing\n")
        return False
    if not dst.exists():
        sys.stderr.write(f"[{name}] cannot refresh prompt: {dst} missing (re-create manually)\n")
        return False

    # preserve existing attribution header (everything up to and including the
    # closing `-->` of the first HTML comment block)
    existing = dst.read_text(encoding="utf-8")
    end = existing.find("-->")
    if end == -1:
        sys.stderr.write(
            f"[{name}] cannot refresh: {dst} has no attribution header. "
            f"Refusing to overwrite blindly.\n"
        )
        return False
    header = existing[: end + len("-->")]
    body = src.read_text(encoding="utf-8")
    dst.write_text(header + "\n\n" + body, encoding="utf-8")
    print(f"[{name}] refreshed prompts/{prompt_filename} from external/{name}/SKILL.md")
    return True


def check_status() -> int:
    print("Checking humanizer install status...")
    all_ok = True
    for name, _, _ in REPOS:
        if (EXTERNAL / name / "SKILL.md").exists():
            print(f"  [OK]   external/{name}/")
        else:
            print(f"  [MISS] external/{name}/")
            all_ok = False
    for _, _, prompt in REPOS:
        if (PROMPTS / prompt).exists():
            print(f"  [OK]   prompts/{prompt}")
        else:
            print(f"  [MISS] prompts/{prompt}")
            all_ok = False
    return 0 if all_ok else 1


def main() -> int:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--check", action="store_true",
                   help="Report install status only; no changes.")
    p.add_argument("--refresh-prompts", action="store_true",
                   help="After install, also overwrite prompts/humanizer-{zh,}.md "
                        "from the freshly-cloned SKILL.md (keeps attribution header).")
    args = p.parse_args()

    if args.check:
        return check_status()

    if not have_git():
        sys.stderr.write("ERROR: git not found in PATH. Install git first.\n")
        return 2

    ok_count = 0
    for name, url, _ in REPOS:
        if install_one(name, url) and verify_install(name):
            ok_count += 1

    if args.refresh_prompts:
        print()
        print("Refreshing vendored prompts/...")
        for name, _, prompt in REPOS:
            refresh_prompt(name, prompt)

    print()
    print(f"Installed {ok_count}/{len(REPOS)} humanizer skills to external/")
    if ok_count == len(REPOS):
        print()
        print("Next steps:")
        print("  - SKILL.md is at external/humanizer-zh/SKILL.md (zh) and external/humanizer/SKILL.md (en)")
        print("  - Per-agent invocation: see skills/humanizer-usage.md")
        print("  - Fallback prompts (no install needed): prompts/humanizer-zh.md, prompts/humanizer.md")

    return 0 if ok_count == len(REPOS) else 1


if __name__ == "__main__":
    sys.exit(main())
