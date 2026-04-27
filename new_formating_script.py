import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_FILE = BASE_DIR / "combined_sales.csv"
INPUT_FILES = [
    DATA_DIR / "daily_sales_data_0.csv",
    DATA_DIR / "daily_sales_data_1.csv",
    DATA_DIR / "daily_sales_data_2.csv",
]


def parse_price(price_text):
    return float(price_text.replace("$", ""))


with OUTPUT_FILE.open("w", newline="") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=["sales", "date", "region"])
    writer.writeheader()

    for input_file in INPUT_FILES:
        with input_file.open("r", newline="") as source_file:
            reader = csv.DictReader(source_file)

            for row in reader:
                price = parse_price(row["price"])
                quantity = int(row["quantity"])
                sales = price * quantity

                writer.writerow(
                    {
                        "sales": f"{sales:.2f}",
                        "date": row["date"],
                        "region": row["region"],
                    }
                )


print(f"Created {OUTPUT_FILE.name}")
