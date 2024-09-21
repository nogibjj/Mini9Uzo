"""
Test your library here!

"""

from mylib.lib import (
    load_data,
    plot_pie_chart,
    summary_stats,
    grab_mean,
    grab_min,
    grab_std,
    grab_max,
    mini_project_2,
)

example_csv = "https://www.kaggle.com/datasets/muhammadehsan02/top-1000-wealthiest-people-in-the-world/data.csv"


def test_load_data():
    """Testing that load data even works"""
    general_df = load_data(example_csv)
    assert general_df is not None
    assert general_df.shape == (1000, 5)


def test_stats():
    """Checking my overall operations on given data"""
    general_df = load_data(example_csv)
    test_mean = grab_mean(general_df, "Net Worth (in billions)")
    test_min = grab_min(general_df, "Net Worth (in billions)")
    test_max = grab_max(general_df, "Net Worth (in billions)")
    test_std = grab_std(general_df, "Net Worth (in billions)")
    test_describe = general_df.describe()
    assert test_describe.loc["mean", "Net Worth (in billions)"] == test_mean
    assert test_describe.loc["std", "Net Worth (in billions)"] == test_std
    assert test_describe.loc["max", "Net Worth (in billions)"] == test_max
    assert test_describe.loc["min", "Net Worth (in billions)"] == test_min
