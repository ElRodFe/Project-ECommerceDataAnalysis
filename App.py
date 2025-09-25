import pandas as pd
import numpy as np
import seaborn as sns

#Create DataFrame and get the shape of it (uncomment the print for visualization)
df = pd.read_csv("data/amazonSalesReport.csv")

#Eliminating spaces in columns names
df.columns = df.columns.str.strip()

print(f"Before Cleaning shape is: {df.shape}")
print()

#print(df.dtypes) #See columns and its data types


    #### Cleaning Data ####

#Drop unusefull columns
df = df.drop(["Unnamed: 22", 
              "fulfilled-by", 
              "B2B", 
              "promotion-ids", 
              "ship-postal-code", 
              "ship-state", 
              "ship-city", 
              "Qty",
              "ASIN",
              "SKU",
              "Style",
              "Order ID",
              "index",
              "ship-country"], axis = 1)

#Drop rows with null values
df = df.dropna()

#Drop Columns with only one unique values (not adding important data for analyzing)
    # This will print columns with only one unique value
for col in df.columns:
    if df[col].nunique() == 1:
        print(col, df[col].unique())
print()
    #Delete those columns
df = df.drop(["Sales Channel", 
              "currency"], axis = 1)

#Reset index for more clarity
df = df.reset_index(drop=True)

print(f"After cleaning shape is: {df.shape}")
print()
              
    #### Rename Columns ####
df = df.rename(columns = {"ship-service-level": "Ship_service_level",
                          "Courier Status": "Courier_status",})

    #### Reorder Columns ####
df = df[["Date", "Status", "Fulfilment", "Amount", "Category", "Size", "Courier_status", "Ship_service_level"]]


