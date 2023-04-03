import pandas as pd
import numpy as np
def load_and_process(path='../data/raw/mexico_listings.csv'):

    # Method Chain 1 (Load data and drop uneccessary columns)

    df1 = (pd.read_csv("../data/raw/Mexico_listings.csv").drop(columns = ["id", "name", "host_id", "host_name", "neighbourhood_group","number_of_reviews","last_review", "reviews_per_month","calculated_host_listings_count","number_of_reviews_ltm","license","availability_365"]))
          

    # Method Chain 2 (drop outlier prices, minimum nights over 15 days, keep only prices over $0, sort by price

    df2 = (df1.drop(df[df['price']>10000].index) .loc[lambda x: x['minimum_nights']<15].loc[lambda x: x['price']>0]
    .assign(price_cad=lambda x: x['price']*0.06472)).sort_values("price", ascending=True).reset_index(drop=True)

    # Make sure to return the latest dataframe

    return df2