# G6-Stock-Predictor

## How to run:
- Save both files *'main.py'* and *'run_main.py'* in the same directory
 - __Run Jupyter from the same directory as *'main.py'*__
   - That is, if *'main.py'* is stored in C:\Users\John\Documents\Project\
   - You must also run jupyter from C:\Users\John\Documents\Project\
 - Make sure you have all the correct python packages (see below for install guide)
 - Execute *'run_main.py'* in the first cell
 - Wait a few minutes for graph output (this takes more time for larger datasets)

- Python package install (command prompt):
  -  pip install --user -U pandas numpy matplotlib sklearn keras tensorflow 

### Initial Commit: 
- Opening CSV file as Pandas DataFrame object (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).
- Shows stock high prices over time.

### Version 0.1.0:
- Line graph for visualisation purposes
- Normalise data
- Create 70-30 train-test data split

### Version 0.2.0:
- Function for creating an array where X is the price of one share, and Y is the price of that share the next day.

### Version 0.3.0:
- raw data aquisition and splitting has been separated 
- LSTM model created
- model fit to training split data
- model tested on test split data
- RMSE scores shown
- graph plotted to show model fit accuracy
- main.py is accessible from another file
