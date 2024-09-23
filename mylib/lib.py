import polars as pl
import matplotlib.pyplot as plt


# Function to load data from a CSV file
def load_data(filepath):
    """This function loads data from a CSV file."""
    data_frame = pl.read_csv("Top_1000_wealthiest_people.csv")
    return data_frame


# Function to plot a pie chart of net worth distribution by industry
def plot_pie_chart(data_frame):
    if type(data_frame) == str:
        data_frame = pl.read_csv(data_frame)
    print(data_frame)
    """This function plots the pie chart."""
    # Group by industry and sum net worth
    # industry_net_worth = data_frame.group_by("Industry").agg(
    # pl.col("Net Worth (in billions)").sum().alias("Total Net Worth (in billions)")
    # )
    # print(industry_net_worth)
    data_frame = pl.DataFrame(data_frame).drop_nulls()
    print(data_frame)
    # Convert to pandas DataFrame for plotting
    industry_net_worth_pd = data_frame.to_pandas()
    industry_net_worth_pd = (
        industry_net_worth_pd.groupby("Industry").sum().reset_index()
    )

    # Plot pie chart
    plt.figure(figsize=(10, 7))
    plt.pie(
        industry_net_worth_pd["Net Worth (in billions)"],
        labels=industry_net_worth_pd["Industry"],
        autopct="%1.1f%%",
    )
    plt.title("Net Worth Distribution by Industry")
    plt.show()


# Function to print summary statistics
def summary_stats(data_frame):
    """This function prints summary statistics."""
    return data_frame.describe()


# Helper functions
def grab_mean(data_frame, col):
    return data_frame[col].mean()


def grab_min(data_frame, col):
    return data_frame[col].min()


def grab_std(data_frame, col):
    return data_frame[col].std()


def grab_max(data_frame, col):
    return data_frame[col].max()


def mini_project_2(filepath):
    """Main function that runs the workflow."""
    data_frame = load_data(filepath)
    plot_pie_chart(data_frame)
    summary_stats(data_frame)
    print(data_frame.shape)
    print(data_frame.describe)
