"""Pipeline mínimo para generar una ficha demo por equipamiento."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from impact_rules import classify_text

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "data" / "demo" / "news_demo.csv"
OUTPUT_FILE = BASE_DIR / "outputs" / "demo_profiles.json"


def build_profiles(df: pd.DataFrame) -> dict:
    df = df.copy()
    df["labels"] = df["text"].apply(classify_text)

    profiles: dict[str, dict] = {}
    for equipment, group in df.groupby("equipment"):
        label_counts: dict[str, int] = {}
        for labels in group["labels"]:
            for label in labels:
                label_counts[label] = label_counts.get(label, 0) + 1

        profiles[equipment] = {
            "equipment": equipment,
            "news_count": int(len(group)),
            "sources": sorted(group["source"].unique().tolist()),
            "impact_dimensions": label_counts,
            "timeline": sorted(group["date"].tolist()),
        }
    return profiles


def main() -> None:
    df = pd.read_csv(INPUT_FILE)
    profiles = build_profiles(df)
    OUTPUT_FILE.write_text(json.dumps(profiles, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Salida generada en: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
