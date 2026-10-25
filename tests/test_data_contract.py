from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "sales_opportunities.csv"

def test_opportunity_dataset_contract():
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert rows
    required = {"OpportunityID", "CreatedDate", "Stage", "AmountEUR"}
    assert required.issubset(rows[0].keys())
    ids = [row["OpportunityID"] for row in rows]
    assert all(ids)
    assert len(ids) == len(set(ids))
    assert all(float(row["AmountEUR"]) >= 0 for row in rows)
