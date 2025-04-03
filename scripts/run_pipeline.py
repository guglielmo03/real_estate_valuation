import os
import sys
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path

import logging
from src import config
from src.load_data import load_data
from src.make_model import train_model_complete, train_model_not_lat_long, train_model_lat_long

# Set up logging
logging.basicConfig(filename='../logs/pipeline.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("Starting Algorithms...")

    # Step 1: Load data from Excel and store it in SQLite
    logging.info("Loading raw data...")
    load_data()

    # Step 3: Train models
    logging.info("Training the model...")
    train_model_complete()
    train_model_not_lat_long()
    train_model_lat_long()

if __name__ == "__main__":
    main()