import sqlite3
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
from src import config

import logging
# Set up logging
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_data():
    logging.info('Opening Excel Files...')
    df = pd.read_excel(os.path.join(config.RAW_DATA_PATH,
                    'Real estate valuation data set.xlsx'))
    df.drop_duplicates(inplace=True) # drop duplicates

    # drop useless variables
    df.drop(columns=["No", "X1 transaction date"], inplace=True)

    # rename variables
    df.rename(columns={"X2 house age": "house_age", 
                   "X3 distance to the nearest MRT station": "distance_nearest_mrt_station",
                   "X4 number of convenience stores": "number_convenience_stores",
                   "X5 latitude": "latitude",
                   "X6 longitude": "longitude",
                   "Y house price of unit area": "y_house_price_unit_area"}, inplace=True)    

    # Create a connection to the SQLite database (or create if it doesn't exist)
    conn = sqlite3.connect(config.DATABASE_PATH)

    # Write the DataFrame to a table (replace 'my_table' with your desired table name)
    df.to_sql(config.RAW_TABLE, conn, if_exists='replace', index=False)

    # Commit and close the connection
    conn.commit()
    conn.close()

    logging.info(f"Data successfully written to {config.RAW_TABLE} table.")
