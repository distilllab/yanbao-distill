# -*- coding: utf-8 -*-
"""find_reports.py -- 按/关键词在量化研报原始库里找 PDF。

用法:
    python find_reports.py 关键词1 [关键词2 ...] [--dir 研报目录]

行为:
- 对目录下所有 .pdf 文件名做不区分大小写的匹配（多关键词为 OR 关系）
- 输出 UTF-8 结果: 序号 | 大小KB | 路径
- 同名/近似重复(归一化后标题相同)会标 [DUP] 并只保留一个主候选
- 退出码: 0=有结果, 1=无结果, 2=目录不存在

注意: 只打印, 不修改任何文件。
"""
import argparse
import os
import re
import sys
import unicodedata
from pathlib import Path

DEFAULT_DIR = os.environ.get("YANBAO_LIBRARY", "")

# 常见噪音词, 归一化时剔除, 用于识别"同一份报告的不同文件名"
NOISE = re.compile(r"[\s_\-()（）\[\]【】:：,，.。·、'\"“”!！?？]+")


def norm_title(name: str) -> str:
    s = unicodedata.normalize("NFKC", name)
    s = NOISE.sub("", s).lower()
    return s


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("keywords", nargs="+")
    ap.add_argument("--dir", default=DEFAULT_DIR)
    args = ap.parse_args()

    if not args.dir:
        print("ERROR: 未配置研报库路径。用 --dir <路径> 或环境变量 YANBAO_LIBRARY 指定。", file=sys.stderr)
        return 2
    root = Path(args.dir)
    if not root.is_dir():
        print(f"ERROR: 目录不存在: {root}", file=sys.stderr)
        return 2

    kws = [k.lower() for k in args.keywords]
    pdfs = sorted(root.glob("*.pdf"))

    matches = []
    for p in pdfs:
        low = p.name.lower()
        if any(k in low for k in kws):
            matches.append(p)

    if not matches:
        print(f"NO_MATCH: 关键词 {kws} 在 {root} 未命中任何 PDF")
        return 1

    # 重复识别: 归一化标题相同 -> 后出现的标 DUP
    seen: dict[str, Path] = {}
    dup_flags: dict[Path, bool] = {}
    for p in matches:
        key = norm_title(p.stem)
        if key in seen:
            dup_flags[p] = True
        else:
            seen[key] = p
            dup_flags[p] = False

    print(f"命中 {len(matches)} 份 (去重后 {len(seen)} 份) 关键词={kws}")
    print("-" * 72)
    for i, p in enumerate(matches, 1):
        kb = p.stat().st_size // 1024
        tag = " [DUP-重复件,跳过]" if dup_flags[p] else ""
        print(f"{i:3d} | {kb:6d} KB | {p.name}{tag}")
        if dup_flags[p]:
            print(f"      └ 与 {seen[norm_title(p.stem)].name} 重复")
    print("-" * 72)
    print("下一步: 由选题分身按 篇幅<=40页/与主线相关/产出可用 三条标准挑 1 份, 用 Read 工具读原始 PDF。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
