#!/usr/bin/env python3
"""Validate the public data package for the Seoul Economic policy news project."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"

REQUIRED = [
    DATA / "web_payload.json",
    DATA / "policy_alignment_status.csv",
    DATA / "policy_alignment_status.json",
    DATA / "policy_alignment.csv",
    DATA / "sector_recipe.csv",
    DATA / "plot_series.csv",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    for path in REQUIRED:
        if not path.exists():
            fail(f"missing {path.relative_to(ROOT)}")

    status = read_csv(DATA / "policy_alignment_status.csv")
    sector = read_csv(DATA / "sector_recipe.csv")
    plot = read_csv(DATA / "plot_series.csv")

    if len(status) != 50:
        fail(f"policy_alignment_status rows expected 50, got {len(status)}")
    if len({row["policy_n"] for row in status}) != 50:
        fail("policy_n is not unique across 50 policies")
    if len({row["sector"] for row in status}) != 5:
        fail("expected 5 sectors")
    if len(sector) != 5:
        fail(f"sector_recipe rows expected 5, got {len(sector)}")
    if len(plot) != 7139:
        fail(f"plot_series rows expected 7139, got {len(plot)}")
    if {row["alignment_status"] for row in status} != {"방향 정합"}:
        fail("alignment_status should be '방향 정합' for the public package")
    weak_count = sum(1 for row in status if row["alignment_grade"] == "약한 정합")
    if weak_count != 4:
        fail(f"weak alignment count expected 4, got {weak_count}")

    payload = json.loads((DATA / "web_payload.json").read_text(encoding="utf-8"))
    expected_keys = {
        "meta",
        "sector_recipe",
        "policy_alignment",
        "policy_alignment_status",
        "plot_series",
    }
    if set(payload) != expected_keys:
        fail(f"web_payload keys mismatch: {sorted(payload)}")
    if len(payload["policy_alignment_status"]) != 50:
        fail("web_payload policy_alignment_status expected 50")
    if len(payload["plot_series"]) != 7139:
        fail("web_payload plot_series expected 7139")
    first_status = payload["policy_alignment_status"][0]
    if not isinstance(first_status["policy_n"], int):
        fail("web_payload policy_alignment_status.policy_n should be numeric")
    if not isinstance(first_status["r"], (int, float)):
        fail("web_payload policy_alignment_status.r should be numeric")

    print("OK: data package is valid")


if __name__ == "__main__":
    main()
