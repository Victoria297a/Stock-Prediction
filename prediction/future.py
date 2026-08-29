from matplotlib.pyplot import plot
from sktime.datasets import load_airline
from sktime.forecasting.base import ForecastingHorizon
from sktime.forecasting.model_selection import temporal_train_test_split
from sktime.forecasting.theta import ThetaForecaster
from sktime.performance_metrics.forecasting import mean_absolute_percentage_error

import pandas as pd

y = load_airline()
"""print(y)
"""
y = pd.DataFrame(load_airline())
y.plot() 
y_train, y_test = temporal_train_test_split(y, test_size = 0.2)
fh = ForecastingHorizon(y_test.index, is_relative=False)
"""print(fh)"""
forecaster = ThetaForecaster(sp=12)
forecaster.fit(y_train)
y_pred = forecaster.predict(fh)
"""print(y_pred)"""
#print(mean_absolute_percentage_error(y_test, y_pred))
plot(y_test, y_pred)
import matplotlib.pyplot as plt
plt.show()