#!/usr/bin/env python3
"""
setup_project_structure.py

Run this script INSIDE your already-cloned repository folder.
It will safely create missing folders and placeholder files without overwriting anything.

Usage:
    python setup_project_structure.py
    # or
    python setup_project_structure.py --force   # to overwrite existing empty files (careful!)
"""

import os
import sys
from pathlib import Path

# ── Structure definition ─────────────────────────────────────────────────────────
# Format: relative_folder → list of files to create in that folder
STRUCTURE = {
    ".": [  # root
        "README.md",
        "requirements.txt",
        ".gitignore",
    ],
    "docs": [
        "01-product.md",
        "02-audience.md",
        "03-competitors.md",
        "04-visual-references.md",
    ],
    "prompts": [
        "hero.txt",
        "features.txt",
        "pricing.txt",
        "testimonials.txt",
        "cta.txt",
        "seo-meta.txt",
    ],
    "src": [],
    "src/styles": [],
    "src/components": [],
    "src/public": [],
    ".antigravity": [
        "agents.json",
        "mcps.json",
    ],
}

# ── Optional initial content for some files ──────────────────────────────────

INITIAL_CONTENT = {
    ".gitignore": """
# Python
__pycache__/
*.pyc
.venv/
.env

# Build / deploy
node_modules/
dist/
build/
.next/
.vercel/

# Antigravity
.antigravity/cache/
    """.strip(),

    "requirements.txt": """
# Only needed if you run Python scripts outside Antigravity
crewai>=0.67.0
anthropic>=0.40.0
python-dotenv>=1.0.0
    """.strip(),
}

# ── Main logic ───────────────────────────────────────────────────────────────

def create_missing_structure(root: Path, force_overwrite_empty: bool = False):
    print(f"Setting up structure in: {root.resolve()}\n")

    created = 0
    skipped = 0

    for rel_folder, files in STRUCTURE.items():
        folder = root / rel_folder
        folder.mkdir(parents=True, exist_ok=True)

        print(f"  Folder: {rel_folder or '.'}")

        for file_name in files:
            target = folder / file_name

            if target.exists():
                if target.stat().st_size == 0 and force_overwrite_empty:
                    print(f"    Overwriting empty file: {target.name}")
                    target.write_text("", encoding="utf-8")
                    created += 1
                else:
                    print(f"    Skipped (already exists): {target.name}")
                    skipped += 1
                continue

            # Create empty file
            target.touch()
            print(f"    Created: {target.name}")
            created += 1

            # Add initial content if defined
            if file_name in INITIAL_CONTENT:
                target.write_text(INITIAL_CONTENT[file_name], encoding="utf-8")
                print(f"      → Added initial content")

    print("\n" + "═" * 60)
    print(f"Setup complete!")
    print(f"  Created: {created} files/folders")
    print(f"  Skipped (already exist): {skipped}")
    print(f"  Project root: {root.resolve()}")
    print("Next steps:")
    print("  1. Fill docs/ with your product information")
    print("  2. Open this folder in Google Antigravity")
    print("  3. Start Agent Manager → dispatch agents!")
    print("═" * 60)


def main():
    root = Path.cwd()

    # Optional --force flag to overwrite empty files
    force = "--force" in sys.argv or "-f" in sys.argv

    if not (root / ".git").is_dir():
        print("Warning: This does not look like a git repository.")
        print("Make sure you run this inside your cloned repo folder.\n")

    try:
        create_missing_structure(root, force_overwrite_empty=force)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()