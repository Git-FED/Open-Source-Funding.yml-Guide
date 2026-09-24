import csv
from pathlib import Path
rows=list(csv.DictReader(Path('DATA/fees.csv').open()))
print('| Platform | Typical total | Notes |')
print('| --- | --- | --- |')
for row in rows:
    print(f"| {row['platform']} | {row['typical_total']} | {row['notes']} |")
