import os
import pandas as pd 

ROOT_PATH = "C:\\Users\\John\\Downloads\\archive\\stocks-50\\"

def load_stock_data(root_path=ROOT_PATH):
    csv_path = os.path.join(root_path, "A.csv")
    return pd.read_csv(csv_path)


stock_data = load_stock_data()


stock_data.plot(kind="line", x="Date", y="High") # Requires Jupyter

