import pandas as pd
import matplotlib.pyplot as plt


# Function to load data from a CSV file
def load_data(filepath):
    """This function loads data from a CSV file."""
    data_frame = pd.read_csv(filepath)
    return data_frame


# Function to plot a pie chart of net worth distribution by industry
def plot_pie_chart(data_frame):
    """This function plots the pie chart."""
    industry_net_worth = data_frame.groupby("Industry")["Net Worth (in billions)"].sum()
    industry_net_worth.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Net Worth Distribution by Industry")
    plt.ylabel("")
    plt.show()


# Function to print summary statistics
def summary_stats(data_frame):
    """This function prints summary statistics."""
    sum_stats = data_frame.describe()
    print(sum_stats)


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
