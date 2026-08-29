# Stock Prediction

A small time-series forecasting exercise using [sktime](https://www.sktime.net/).

`prediction/future.py` fits a `ThetaForecaster` to the classic Box-Jenkins airline
passengers dataset (`sktime`'s built-in `load_airline`), splits it into train/test
sets, forecasts the held-out period, and plots the forecast against the actual
values.

## What it does

1. Loads the airline passengers dataset.
2. Splits it into 80% train / 20% test (`temporal_train_test_split`).
3. Fits a `ThetaForecaster` (seasonal period = 12, i.e. monthly data) on the
   training set.
4. Forecasts the test period and plots the forecast against the actual values
   with `matplotlib`.

## Setup

```bash
pip install sktime pandas matplotlib
```

## Run

```bash
python prediction/future.py
```

A plot window will open comparing the forecasted values to the actual test data.

## Next steps

- Report forecast accuracy with `mean_absolute_percentage_error` (already imported,
  not yet printed).
- Try alternative forecasters (e.g. `AutoARIMA`, exponential smoothing) for comparison.
- Apply the same pipeline to a real-world financial time series instead of the
  airline dataset.
