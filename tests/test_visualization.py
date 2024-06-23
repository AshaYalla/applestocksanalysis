import pytest
import pandas as pd
from my_package.src.visualization import StockVisualizer


@pytest.fixture
def mock_data():
    return pd.DataFrame(
        {
            "Date": ["2023-01-01", "2023-01-02"],
            "AAPL.Open": [100, 102],
            "AAPL.High": [105, 107],
            "AAPL.Low": [99, 101],
            "AAPL.Close": [102, 105],
        }
    )


def test_create_candlestick_chart(mock_data):
    visualizer = StockVisualizer(mock_data)
    fig = visualizer.create_candlestick_chart()
    assert fig is not None
