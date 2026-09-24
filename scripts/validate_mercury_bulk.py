#!/usr/bin/env python3
"""Fast structural validation for Mercury custom-move bulk batches."""
from __future__ import annotations
import argparse,csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PLAN=ROOT/"manifests"/"MERCURY_CUSTOM_MOVE_BATCH_PLAN.csv"

OFFICIAL_TYPES={"Normal","Fire","Water","Electric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dragon","Dark","Steel","Fairy"}
SOURCE_NATIVE_CUSTOM_TYPES={"Sound","Qmarks","Shadow","Nuclear","Crystal","???"}
CATS={"Physical","Special","Status"}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--batch",default="all"); args=ap.parse_args()
    with PLAN.open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    if args.batch!="all": rows=[r for r in rows if r["batch_id"]==args.batch]
    if not rows: raise SystemExit("No rows selected")

    errors=[]; ids=set(); move_ids=set(); custom_type_rows=[]
    for r in rows:
        n=int(r["provisional_ds_id"])
        if n in ids: errors.append(f"duplicate provisional ID {n}")
        ids.add(n)
        if r["move_id"] in move_ids: errors.append(f"duplicate move ID {r['move_id']}")
        move_ids.add(r["move_id"])

        if r["type"] not in OFFICIAL_TYPES and r["type"] not in SOURCE_NATIVE_CUSTOM_TYPES:
            errors.append(f"{r['move_id']}: unknown type {r['type']}")
        elif r["type"] in SOURCE_NATIVE_CUSTOM_TYPES:
            custom_type_rows.append(r)

        if r["category"] not in CATS: errors.append(f"{r['move_id']}: bad category {r['category']}")
        if not r["move_name"]: errors.append(f"{r['move_id']}: missing name")

        complete=r["mechanics_audit_status"].lower()=="complete"
        if complete:
            try:
                if int(r["pp"])<=0: raise ValueError
            except ValueError:
                errors.append(f"{r['move_id']}: complete record has invalid PP {r['pp']}")
        elif r["visual_policy"]!="BLOCKED_MECHANICS":
            errors.append(f"{r['move_id']}: incomplete mechanics must be BLOCKED_MECHANICS")

        for key in ("power","accuracy"):
            if r[key]:
                try: int(r[key])
                except ValueError: errors.append(f"{r['move_id']}: invalid {key} {r[key]}")

    if args.batch!="all" and len({r["batch_id"] for r in rows})==1:
        nums=[int(r["provisional_ds_id"]) for r in rows]
        if nums!=list(range(nums[0],nums[0]+len(nums))): errors.append("IDs are not contiguous/in order")

    if errors:
        for e in errors: print("ERROR:",e)
        raise SystemExit(1)

    blocked=sum(r["mechanics_audit_status"].lower()!="complete" for r in rows)
    ready=len(rows)-blocked
    print(f"PASS: {len(rows)} rows structurally valid; {ready} mechanics-ready; {blocked} quarantined blocker(s).")
    if custom_type_rows:
        labels=", ".join(sorted({r["type"] for r in custom_type_rows}))
        print(f"REVIEW: {len(custom_type_rows)} source-native custom-type candidate(s) ({labels}); preserve for source audit, remap/approve separately for Mercury.")

if __name__=="__main__": main()
