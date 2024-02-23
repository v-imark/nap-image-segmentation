import csv
from pathlib import Path


def save_filter_data(total, filtered, thresh, output_path):
    csv_data = [["total", "filtered", "threshold"], [len(total), len(filtered), thresh]]
    with open(Path(output_path, "filterdata.csv"), "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_data)
