#!/usr/bin/env python3
"""Validate required note sections, mode-specific assets, image links, and math delimiters."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED = {
    "summary": ("## 📜 研究核心", "## 🔁 研究内容", "## 🧠 文献价值", "## 🤔 阅读总结"),
    "deep": ("## 🧭 01｜论文定位", "## 🧠 02｜研究逻辑", "## 📚 03｜背景与问题", "## 🧮 04｜理论、方法与公式", "## 🔬 05｜实验/数值设计与证据链", "## 🖼️ 06｜图表精读", "## 🧩 07｜结论边界与批判性分析", "## 💡 08｜研究迁移与最终精读结论"),
}
IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^)]*['\"])?\)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("note", type=Path)
    parser.add_argument("--mode", choices=REQUIRED, required=True)
    args = parser.parse_args()
    note, errors = args.note.resolve(), []
    if not note.is_file():
        errors.append(f"note not found: {note}")
        text = ""
    else:
        text = note.read_text(encoding="utf-8")
        if not (text.lstrip().startswith("---") and "\n---" in text): errors.append("missing YAML frontmatter")
        if "<h1" not in text.lower() and not re.search(r"^#\s+", text, re.M): errors.append("missing document title")
        if "research_direction:" not in text: errors.append("missing research_direction frontmatter")
        for section in REQUIRED[args.mode]:
            if section not in text: errors.append(f"missing required section: {section}")
        prohibited = "assets/deep-figures/" if args.mode == "summary" else "assets/summary-figures/"
        if prohibited in text: errors.append(f"cross-mode asset link: {prohibited}")
        if "assets/figures/" in text: errors.append("obsolete shared asset directory: assets/figures/")
        for line_no, line in enumerate(text.splitlines(), 1):
            count = line.count("$$")
            if "$$$" in line: errors.append(f"line {line_no}: invalid $$$ delimiter")
            if count not in (0, 2): errors.append(f"line {line_no}: display math must be one $$...$$ pair")
        for raw in IMAGE.findall(text):
            relative = raw.strip("<>").split("#", 1)[0]
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", relative): continue
            asset = (note.parent / relative).resolve()
            try: asset.relative_to(note.parent.resolve())
            except ValueError: errors.append(f"image escapes note folder: {raw}"); continue
            if not asset.is_file(): errors.append(f"missing image asset: {raw}")
    report = {"note": str(note), "mode": args.mode, "valid": not errors, "errors": errors}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
