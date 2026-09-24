"""Manual-review helper: prints rows that need a new verification date."""
import csv
from pathlib import Path
from datetime import date
rows=list(csv.DictReader(Path('DATA/fees.csv').open()))
for row in rows:
    print(f"{row['platform']}: last verified {row['last_verified']} — review official terms before release")
print(f"Review date: {date.today().isoformat()}")
