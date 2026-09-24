#!/usr/bin/env python3
"""Build/check Mercury Redux compact candidate IDs and 50-move bulk batches."""
from __future__ import annotations
import argparse, csv, io, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
COMMUNITY=ROOT/"manifests"/"community_moves.csv"
AUDIT=ROOT/"manifests"/"FULL_MOVE_APPROVAL_DETAILS.csv"
CONSTANTS=ROOT/"constants"/"moves_post_gen4.h"
OUT=ROOT/"manifests"/"MERCURY_CUSTOM_MOVE_BATCH_PLAN.csv"
BATCH_OUT=ROOT/"manifests"/"MERCURY_CUSTOM_MOVE_BATCH_SUMMARY.csv"
BATCH_SIZE=50
PLAN_COLUMNS=["candidate_index","provisional_ds_id","batch_id","move_id","move_name","type","category","power","accuracy","pp","mechanics_audit_status","animation_class","animation_reference","visual_policy"]
SUMMARY_COLUMNS=["batch_id","count","id_start","id_end","blocked","defer_until_approved","unique_donor_visual_once_after_port","no_per_move_visual_donor_spot_check"]

def read_csv(path):
    with path.open(newline="",encoding="utf-8") as f: return list(csv.DictReader(f))
def official_max_id():
    text=CONSTANTS.read_text(encoding="utf-8")
    ids=[int(x) for x in re.findall(r"^\s*#define\s+MOVE_[A-Z0-9_]+\s+(\d+)\s*$",text,re.M)]
    if not ids: raise SystemExit("No move IDs found")
    return max(ids)
def visual_policy(a):
    mech=(a.get("mechanics_audit_status") or "").lower()
    cls=(a.get("ds_animation_class") or "").lower()
    if mech!="complete": return "BLOCKED_MECHANICS"
    if "platinum/base-era" in cls: return "NO_PER_MOVE_VISUAL_DONOR_SPOT_CHECK"
    if "hg-engine" in cls or (a.get("ds_animation_path") or ""): return "UNIQUE_DONOR_VISUAL_ONCE_AFTER_PORT"
    return "DEFER_VISUAL_UNTIL_APPROVED"
def render(rows,cols):
    s=io.StringIO(newline=""); w=csv.DictWriter(s,fieldnames=cols,quoting=csv.QUOTE_ALL,lineterminator="\n"); w.writeheader(); w.writerows(rows); return s.getvalue()
def build():
    moves=read_csv(COMMUNITY); audit={r["move_id"]:r for r in read_csv(AUDIT)}
    if len(moves)!=519: raise SystemExit(f"Expected 519 candidates, found {len(moves)}")
    start=official_max_id()+1; rows=[]
    for i,m in enumerate(moves):
        a=audit.get(m["move_id"],{})
        rows.append({
            "candidate_index":i+1,"provisional_ds_id":start+i,"batch_id":f"BULK{(i//BATCH_SIZE)+1:02d}",
            "move_id":m["move_id"],"move_name":m["move_name"],"type":m["type"],"category":m["category"],
            "power":m["power"],"accuracy":m["accuracy"],"pp":m["pp"],
            "mechanics_audit_status":a.get("mechanics_audit_status","missing"),
            "animation_class":a.get("ds_animation_class",""),"animation_reference":a.get("animation_reference",""),
            "visual_policy":visual_policy(a)})
    sums=[]
    for b in range(1,(len(rows)+BATCH_SIZE-1)//BATCH_SIZE+1):
        bid=f"BULK{b:02d}"; rs=[r for r in rows if r["batch_id"]==bid]
        sums.append({"batch_id":bid,"count":len(rs),"id_start":rs[0]["provisional_ds_id"],"id_end":rs[-1]["provisional_ds_id"],
            "blocked":sum(r["visual_policy"]=="BLOCKED_MECHANICS" for r in rs),
            "defer_until_approved":sum(r["visual_policy"]=="DEFER_VISUAL_UNTIL_APPROVED" for r in rs),
            "unique_donor_visual_once_after_port":sum(r["visual_policy"]=="UNIQUE_DONOR_VISUAL_ONCE_AFTER_PORT" for r in rs),
            "no_per_move_visual_donor_spot_check":sum(r["visual_policy"]=="NO_PER_MOVE_VISUAL_DONOR_SPOT_CHECK" for r in rs)})
    return render(rows,PLAN_COLUMNS),render(sums,SUMMARY_COLUMNS),start,start+len(rows)-1
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); args=ap.parse_args()
    plan,summary,start,end=build()
    if args.check:
        stale=[]
        if not OUT.exists() or OUT.read_text(encoding="utf-8")!=plan: stale.append(str(OUT.relative_to(ROOT)))
        if not BATCH_OUT.exists() or BATCH_OUT.read_text(encoding="utf-8")!=summary: stale.append(str(BATCH_OUT.relative_to(ROOT)))
        if stale: raise SystemExit("Stale generated plan: "+", ".join(stale))
        print(f"PASS: 519 candidates staged at provisional IDs {start}-{end}."); return
    OUT.write_text(plan,encoding="utf-8"); BATCH_OUT.write_text(summary,encoding="utf-8")
    print(f"Wrote 519 candidates at provisional IDs {start}-{end} in 11 bulk batches.")
if __name__=="__main__": main()
