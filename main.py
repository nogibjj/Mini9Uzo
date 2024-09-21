"""This code is for main.py; it reads a dataset and prints some summary info about it!"""

import pandas as pd
from mylib.lib import load_data, plot_pie_chart, summary_stats

# Constant for the CSV file path
CSV_FILE = "Top_1000_wealthiest_people.csv"


def main():
    data_frame = load_data(CSV_FILE)
    plot_pie_chart(data_frame)
    summary_stats(data_frame)


# Need this to update the actual values for IO string in Test
df = pd.read_csv(CSV_FILE)
industry_net_worth = df.groupby("Industry")["Net Worth (in billions)"].sum()
print(industry_net_worth)
print(str(df))


if __name__ == "__main__":
    main()
