#!/usr/bin/env python3
"""Detect exact and functional duplicate move candidates in the Mercury catalog."""
from __future__ import annotations
import argparse,csv,re
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/"manifests"/"FULL_MOVE_APPROVAL_DETAILS.csv"

def read_rows():
    with AUDIT.open(newline="",encoding="utf-8") as f:
        return list(csv.DictReader(f))

def norm(value: str) -> str:
    value=(value or "").lower().replace("pokémon","pokemon")
    value=re.sub(r"\s+"," ",value).strip()
    return value

def norm_priority(value: str) -> str:
    m=re.search(r"[+-]?\d+",value or "")
    return m.group(0) if m else "0"

def norm_target(value: str) -> str:
    s=norm(value)
    if "all adjacent foes" in s or "both opposing" in s:
        return "all-foes"
    if "all adjacent pokemon" in s:
        return "all-adjacent"
    if "one adjacent" in s or "one target" in s or "one pokemon other" in s:
        return "single"
    if s in {"the user","user","self"}:
        return "self"
    return s

def norm_effect(value: str, strip_pp: bool=False) -> str:
    s=norm(value)
    if strip_pp:
        s=re.sub(r"\b\d+\s*pp\b","PP",s)
    return s

def signature(r, ignore_pp=False):
    return (
        norm(r["type"]), norm(r["category"]), r["power"], r["accuracy"],
        "" if ignore_pp else r["pp"],
        norm_priority(r["priority"]), norm_target(r["target"]), norm(r["contact"]),
        norm(r["move_flags"]), norm_effect(r["what_it_does"],strip_pp=ignore_pp),
        norm(r["effect_chance"]), norm(r["status_effects"]), norm(r["stat_changes"]),
        norm(r["multi_hit_or_duration"]), norm(r["recoil"]), norm(r["drain_or_healing"]),
        norm(r["switching_behavior"]), norm(r["field_weather_terrain_behavior"])
    )

def find_groups(rows,ignore_pp=False):
    groups=defaultdict(list)
    for r in rows:
        groups[signature(r,ignore_pp)].append(r)
    return [g for g in groups.values() if len(g)>1]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--strict",action="store_true",help="exit nonzero when exact duplicates are found")
    args=ap.parse_args()
    rows=read_rows()
    exact=find_groups(rows,False)
    functional=find_groups(rows,True)

    print(f"Rows: {len(rows)}")
    print(f"Exact duplicate groups: {len(exact)}")
    for g in exact:
        print("  EXACT:", " / ".join(f"{r['move_id']} ({r['english_review_name']})" for r in g))

    # Functional grouping is conservative and only ignores PP; exact groups are omitted.
    exact_sets={frozenset(r["move_id"] for r in g) for g in exact}
    functional=[g for g in functional if frozenset(r["move_id"] for r in g) not in exact_sets]
    print(f"Functional duplicate groups (PP-only difference): {len(functional)}")
    for g in functional:
        print("  FUNCTIONAL:", " / ".join(f"{r['move_id']} ({r['english_review_name']}, {r['pp']} PP)" for r in g))

    if args.strict and exact:
        raise SystemExit(1)

if __name__=="__main__":
    main()
