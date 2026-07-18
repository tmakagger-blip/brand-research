#!/usr/bin/env python3
"""Rank a sampled social-listening CSV; do not claim platform-wide popularity."""
from __future__ import annotations
import argparse, csv, math
from pathlib import Path

def number(value: str | None) -> float:
    text = (value or "").strip().lower().replace(",", "")
    if not text or text in {"?", "like", "likes", "??"}: return 0.0
    for suffix, multiplier in {"?": 10000.0, "w": 10000.0, "k": 1000.0}.items():
        if text.endswith(suffix):
            try: return float(text[:-len(suffix)]) * multiplier
            except ValueError: return 0.0
    try: return float(text)
    except ValueError: return 0.0

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("input_csv", type=Path)
    p.add_argument("output_csv", type=Path)
    p.add_argument("--half-life-hours", type=float, default=72.0)
    a = p.parse_args()
    with a.input_csv.open("r", encoding="utf-8-sig", newline="") as f: rows = list(csv.DictReader(f))
    if not rows: raise SystemExit("Input CSV contains no rows")
    raw = [math.log1p(number(r.get("likes")) + 2*number(r.get("saves")) + 3*number(r.get("comments")) + 3*number(r.get("shares"))) for r in rows]
    maximum = max(raw) or 1.0
    for row, score in zip(rows, raw):
        age = max(number(row.get("age_hours")), 0.0)
        relevance = max(0.0, min(1.0, number(row.get("relevance"))/100.0))
        recency = math.exp(-math.log(2)*age/max(a.half_life_hours, 1.0))
        row["hot_score"] = f"{100*(0.55*score/maximum + 0.25*recency + 0.20*relevance):.2f}"
    rows.sort(key=lambda r: float(r["hot_score"]), reverse=True)
    a.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with a.output_csv.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

if __name__ == "__main__": main()
