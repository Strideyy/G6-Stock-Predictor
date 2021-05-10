# G6-Stock-Predictor


## Initial Commit: 
- Opening CSV file as Pandas DataFrame object (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).
- Shows stock high prices over time.

## Version 0.1.0:
- Line graph for visualisation purposes
- Normalise data
- Create 70-30 train-test data split

## Version 0.2.0:
- Function for creating an array where X is the price of one share, and Y is the price of that share the next day.

## Version 0.3.0:
- raw data aquisition and splitting has been separated 
- LSTM model created
- model fit to training split data
- model tested on test split data
- RMSE scores shown
- graph plotted to show model fit accuracy
- main.py is accessible from another file
