
# Apple Stock Data Processor and Visualizer

This Python package processes and visualizes Apple stock data from a CSV file.

## Installation

1. Ensure you have Python 3.7 or later installed.

2. Install the package using pip:
```sh
pip install dist/my_package-0.1.0-py3-none-any.whl
```


## Usage

### Data Processing

Initialize the DataProcessor and load data:
```python
from my_package.data_processing import DataProcessor

DATA_FILE_PATH = 'path/to/your/data.csv'
processor = DataProcessor(DATA_FILE_PATH)
processor.load_data()
```

### Compute Statistics
```python
max_value, min_value, average_value = processor.compute_statistics()
```

### filter data by average volume:
```python
filtered_data = processor.filter_by_average_volume()
```

### Add the day of the week
```python
data_with_day = processor.add_day_of_week()
```

## Data Visualization
### Visualize data using StockVisualizer:
```python
from my_package.visualization import StockVisualizer


visualizer = StockVisualizer(filtered_data)  # Use filtered_data or another DataFrame
fig = visualizer.create_candlestick_chart()
fig.show()
```
## Running the Script

You can use the main.py script to execute the data processing and visualization workflow. Here are the instructions:

Place your data CSV file in the appropriate path.

Modify the main.py script if necessary to point to your data file.

### Run the script:
```sh
python main.py
```

## Running Tests
### Install pytest if you haven't already:
```python
pip install pytest
```

### Run tests
```python
pytest tests/
```




## Code Style

Install flake8 and black if you haven't already:

```sh
pip install flake8 black
```
### Check for PEP 8 compliance:

```
flake8 src/ tests/
```

### Format code using black:
```
black src/ tests/
```


## Verify the Wheel:
   To ensure everything works correctly, you can create a virtual environment and install the wheel file:
   ```sh
   python -m venv test_env
   source test_env/bin/activate  
   pip install dist/avenuecode_apple_python_exercise_praveen_thanniru-1.0.0-py3-none-any.whl
```


