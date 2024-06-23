import pandas as pd


def aggregate_weekly_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates Apple stock data to a weekly level.

    Parameters:
    - data (pd.DataFrame): DataFrame containing the Apple stock data.

    Returns:
    - weekly_data (pd.DataFrame): Weekly aggregated DataFrame.
    """
    # Ensure the 'Date' column is in datetime format and set it as the index
    data["Date"] = pd.to_datetime(data["Date"])
    data.set_index("Date", inplace=True)
    # print(data)

    # Resample weekly
    weekly_data = (
        data.resample("W")
        .agg({"AAPL.Close": "mean", "AAPL.Volume": "sum"})
        .reset_index()
    )

    # Rename columns for clarity
    weekly_data.rename(
        columns={
            "Date": "Week_Start_Date",
            "AAPL.Close": "Average_Close_Price",
            "AAPL.Volume": "Total_Volume",
        },
        inplace=True,
    )

    return weekly_data
