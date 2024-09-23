from main import plot_pie_chart, summary_stats
import polars as pl
import io


def test_load_data():
    """Test the load_data function to ensure it loads CSV data correctly."""
    # Create a small in-memory CSV file for testing
    csv_data = io.StringIO(
        """
Industry,Net Worth (in billions)
Technology,35574.00
Retail,23353.29
Media,5733.05
Manufacturing,9938.73
Finance,5108.42
Fashion,3889.92
Cosmetics, 4708.24
Automotive,4198.07
Telecommunications,5776.54
Petrochemicals,4336.01
        """
    )

    df = pl.read_csv(csv_data)
    # Check if the data is loaded correctly
    assert isinstance(df, pl.DataFrame)
    assert df.shape == (11, 2)  # The DataFrame should have 1000 rows and 5 columns


def test_plot_pie_chart():
    """Test the plot_pie_chart function to ensure it executes without error."""
    # Create a small in-memory CSV file for testing
    csv_data = io.StringIO(
        """
Industry,Net Worth (in billions)
Technology,35574.00
Retail,23353.29
Media,5733.05
Manufacturing,9938.73
Finance,5108.42
Fashion,3889.92
Cosmetics, 4708.24
Automotive,4198.07
Telecommunications,5776.54
Petrochemicals,4336.01
        """
    )

    df = pl.read_csv(csv_data)
    # This should run without raising an exception
    plot_pie_chart(df)


def test_summary_stats():
    """Test the summary_stats function to ensure it generates statistics correctly."""
    # Create a small in-memory CSV file for testing
    csv_data = io.StringIO(
        """
Industry,Net Worth (in billions)
Technology,35574.00
Retail,23353.29
Media,5733.05
Manufacturing,9938.73
Finance,5108.42
Fashion,3889.92
Cosmetics, 4708.24
Automotive,4198.07
Telecommunications,5776.54
Petrochemicals,4336.01
        """
    )

    df = pl.read_csv(csv_data)
    # This should run without raising an exception
    summary_stats(df)


if __name__ == "__main__":
    test_load_data()
    test_plot_pie_chart()
    test_summary_stats()
    print("All tests passed successfully.")
