import pandas as pd
import numpy as np


def load_and_process(path: str,fx_rate: float,top: int = 10,min_price=10,max_price=1000,min_nights=30):
    """
    Calculates and prints a dataset with only data of interest from a standard AirBnB rental listing by city. 

    Parameters:
    path (str): The import path of the AirBnB rental listing dataframe.
    fx_rate (float): The foreign exchange rate from the specified foreign currency to Canadian Dollars.
    top (int): Defines the top neighbourhoods of interest in term of number of listings. Default value is equal to 10.
    min_price: User-defined appropriate minimum price per night, in Canadian Dollars, for the listings in neighbourhoods of interest. Default value is equal to 10.
    max_price: User-defined appropriate maximum price per night, in Canadian Dollars, for the listings in neighbourhoods of interest. Default value is equal to 1000.
    min_nights: User-defined appropriate minimum nights stay in the given city. Default value is equal to 30.

    Returns:
    Filtered dataset based on the given arguments

    """
    
    
    # Check for valid data types for mandatory inputs 
    
    assert (type(path)==str), "Please make sure you are entering a valid file path as a string item."
    assert (type(fx_rate)==float), "Please make sure you are entering a valid foreign exchange rate (foreign currency to CAD) as a float."
    
    # Load data and drop uneccessary columns

    df1 = pd.read_csv(path).drop(['id','host_id','neighbourhood_group', 'license','room_type','number_of_reviews','last_review','reviews_per_month','calculated_host_listings_count','availability_365','number_of_reviews_ltm','host_name'],axis=1)

    # Pick up the top (with a specified number, default at 10) neighbourhoods with the most rental listings
    
    df2=df1.groupby('neighbourhood').count().reset_index().nlargest(top,'name').reset_index(drop=True)
    df2=df2.drop(index=df2.index[top:])
    # Filter the cleaned dataset with the top neighbourhoods of interest
    
    top_neigh=df2["neighbourhood"].unique().tolist()
    df3 = df1.loc[lambda x : x['neighbourhood'].isin(top_neigh)]

    # Assign new columns PricePerNight and Price_CAD to help with analysis
    
    df4=df3.assign(PricePerNight=lambda x: x['price']/x['minimum_nights'])\
    .assign(Price_CAD=lambda x: x['PricePerNight'] * fx_rate)
    
    # Drop listings that requires minimum nights beyond a regular travel duration, and any Price per Night in CAD that are abnormal
    
    df5=df4.drop(df4[df4['minimum_nights']>min_nights].index)\
    .loc[lambda x : x['Price_CAD']>min_price]\
    .loc[lambda x : x['Price_CAD']<max_price]\
    .reset_index(drop=True)



    return df5