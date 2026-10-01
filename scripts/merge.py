"""Merge base + extra into data/hgsi_all.jsonl (shuffled with a fixed seed)."""
import json, random
from pathlib import Path

data = Path(__file__).resolve().parent.parent / "data"
rows = []
for name in ["hgsi_ccd_conversations.jsonl", "hgsi_ccd_conversations_extra.jsonl"]:
    rows += [json.loads(l) for l in open(data / name, encoding="utf-8")]
random.Random(42).shuffle(rows)
with open(data / "hgsi_all.jsonl", "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("merged rows:", len(rows))
