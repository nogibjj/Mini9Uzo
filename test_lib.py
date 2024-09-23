"""
Test your library here!

"""

import io
import polars as pl
from mylib.lib import (
    load_data,
    grab_mean,
    grab_min,
    grab_std,
    grab_max,
)

csv_data = "Top_1000_wealthiest_people.csv"


def test_load_data():
    """Testing that load data even works"""
    csv_data = io.StringIO(
        """
Industry,Net Worth (in billions)
Technology,1300
Retail,850
Media,105
Manufacturing,160
Finance,170
Fashion,130
Cosmetics,99
Automotive,109
Telecommunications,135
Petrochemicals,101
        """
    )
    general_df = pl.read_csv(csv_data)
    assert general_df is not None
    assert general_df.shape == (10, 2)  # 10 Industries and 2 columns


def test_stats():
    """Checking my overall operations on given data"""
    csv_data = io.StringIO(
        """
Industry,Net Worth (in billions)
Technology,1300
Retail,850
Media,105
Manufacturing,160
Finance,170
Fashion,130
Cosmetics,99
Automotive,109
Telecommunications,135
Petrochemicals,101
        """
    )
    general_df = load_data(csv_data)
    test_mean = grab_mean(general_df, "Net Worth (in billions)")
    test_min = grab_min(general_df, "Net Worth (in billions)")
    test_max = grab_max(general_df, "Net Worth (in billions)")
    test_std = grab_std(general_df, "Net Worth (in billions)")
    test_describe = general_df.describe()
    assert test_describe.loc["mean", "Net Worth (in billions)"] == test_mean
    assert test_describe.loc["std", "Net Worth (in billions)"] == test_std
    assert test_describe.loc["max", "Net Worth (in billions)"] == test_max
    assert test_describe.loc["min", "Net Worth (in billions)"] == test_min


if __name__ == "__main__":
    test_load_data()
    test_stats()
