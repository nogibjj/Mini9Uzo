"""This code is for main.py; it reads a dataset and prints some summary info about it!"""

import polars as pl
from mylib.lib import load_data, plot_pie_chart, summary_stats

# Constant for the CSV file path
CSV_FILE = "Top_1000_wealthiest_people.csv"


def main():
    data_frame = load_data(CSV_FILE)
    plot_pie_chart(data_frame)
    summary_stats(data_frame)
    print(data_frame.shape)
    print(data_frame.describe)

    # Group by industry and sum net worth
    industry_net_worth = data_frame.group_by("Industry").agg(
        [pl.col("Net Worth (in billions)").sum()]
    )
    print(industry_net_worth)


if __name__ == "__main__":
    main()
