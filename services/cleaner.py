import pandas as pd

def load_deals():
    return pd.read_csv("data/deals.csv")

def load_work_orders():
    return pd.read_csv("data/work_orders.csv")