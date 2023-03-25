import pandas as pd
import numpy as np

def load_and_process(path='../data/raw/montreal_listings.csv'):
    df1 = (
    pd.read_csv('../data/raw/montreal_listings.csv')
    .drop(columns = ["id", "name", "host_id", "host_name", "neighbourhood_group","number_of_reviews","last_review", "reviews_per_month"
                     ,"calculated_host_listings_count","number_of_reviews_ltm","license","availability_365"])
    .dropna(subset = ['latitude','longitude','price','minimum_nights'])
    .reset_index(drop=True)
    )
    
#(Set parameters for minimum_nights, price)
    df2 = (
        df1.loc[(df_clean2['minimum_nights'] >= 1) & (df_clean2['minimum_nights'] <= 14)]
        .loc[(df_clean2['price'] > 0)]
        .loc[(df_clean2['price'] < 800)]
    )
    
#(Add new price x minimum_nights column)
    df3 = (
        df2.assign(Price_x_Minimum_Nights=lambda x: round(x['price']*x['minimum_nights'], 2))
    .sort_values("Price_x_Minimum_Nights", ascending=True)
    .reset_index(drop=True)
    )
    
#(Return the latest dataframe)
    return df3