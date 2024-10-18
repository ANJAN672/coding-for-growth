import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    newDF = pd.merge(customers, orders, left_on = 'id', right_on = 'customerId', how = 'left')
    newDF = newDF[newDF['customerId'].isna()]
    return newDF[['name']].rename(columns={'name':'Customers'})

