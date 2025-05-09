import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import os
import sys
import pickle
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path
from src import config
import logging

def load_data(): # crea un dataframe partendo da sqlLite
    """Loads data from the SQLite database."""
    conn = sqlite3.connect(config.DATABASE_PATH)
    query = f"SELECT * FROM {config.RAW_TABLE}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def train_model_complete(grid_search=False):
    """Trains a Random Forest model with GridSearchCV and saves evaluation metrics to CSV."""
    df = load_data()

    # Save original indices before vectorization
    df_indices = df.index

    X = df[["house_age", "distance_nearest_mrt_station", "number_convenience_stores", "latitude", "longitude"]]
    y = df['y_house_price_unit_area']

    # Train-test split (preserve indices)
    X_train, X_test, y_train, y_test, train_idx, test_idx = train_test_split(
        X, y, df_indices, test_size=0.2, random_state=42
    )

    if grid_search:
        rf = RandomForestRegressor(random_state=42)
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 5, 10]
        }

        grid_search = GridSearchCV(rf, param_grid, cv=3, scoring='mean_absolute_error', n_jobs=-1, verbose=1)
        grid_search.fit(X_train, y_train)

        best_model = grid_search.best_estimator_
        y_pred = best_model.predict(X_test)
    
    else:
        rf = RandomForestRegressor()
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)

    # salviamo il modello
    with open(os.path.join(config.MODELS_PATH, "random_forest_complete.pickle"), "wb") as file:
        pickle.dump(rf, file)

    # Create a DataFrame for the test set with predictions
    test_df = df.loc[test_idx].copy()  # Copy test set rows
    test_df['prediction'] = y_pred  # Add predictions


    # Compute metrics
    metrics = {
        'accuracy': mean_absolute_error(y_test, y_pred),
        "r2": r2_score(y_test, y_pred)
    }

    # Connect to the database
    conn = sqlite3.connect(config.DATABASE_PATH)

    # saving predictions
    test_df.to_sql(config.PREDICTIONS_TABLE, conn, if_exists='replace', index=False)
    
    # saving grid search results
    metrics_df = pd.DataFrame([metrics])
    metrics_df.to_sql(config.EVALUATION_TABLE, conn,
                      if_exists='replace', index=False)
    # Commit and close the connection
    conn.commit()
    conn.close()

def train_model_not_lat_long(grid_search=False):
    """Trains a Random Forest model with GridSearchCV and saves evaluation metrics to CSV."""
    df = load_data()

    # Save original indices before vectorization
    df_indices = df.index

    X = df[["house_age", "distance_nearest_mrt_station", "number_convenience_stores"]]
    y = df['y_house_price_unit_area']

    # Train-test split (preserve indices)
    X_train, X_test, y_train, y_test, train_idx, test_idx = train_test_split(
        X, y, df_indices, test_size=0.2, random_state=42
    )

    if grid_search:
        rf = RandomForestRegressor(random_state=42)
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 5, 10]
        }

        grid_search = GridSearchCV(rf, param_grid, cv=3, scoring='accuracy', n_jobs=-1, verbose=1)
        grid_search.fit(X_train, y_train)

        best_model = grid_search.best_estimator_
        y_pred = best_model.predict(X_test)
    
    else:
        rf = RandomForestRegressor()
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)

    # salviamo il modello
    with open(os.path.join(config.MODELS_PATH, "random_forest_not_lat_long.pickle"), "wb") as file:
        pickle.dump(rf, file)

    # Create a DataFrame for the test set with predictions
    test_df = df.loc[test_idx].copy()  # Copy test set rows
    test_df['prediction'] = y_pred  # Add predictions


    # Compute metrics
    metrics = {
        'accuracy': mean_absolute_error(y_test, y_pred),
        "r2": r2_score(y_test, y_pred)
    }

    # Connect to the database
    conn = sqlite3.connect(config.DATABASE_PATH)

    # saving predictions
    test_df.to_sql(config.PREDICTIONS_TABLE, conn, if_exists='replace', index=False)
    
    # saving grid search results
    metrics_df = pd.DataFrame([metrics])
    metrics_df.to_sql(config.EVALUATION_TABLE, conn,
                      if_exists='replace', index=False)
    # Commit and close the connection
    conn.commit()
    conn.close()

def train_model_lat_long(grid_search=False):
    """Trains a Random Forest model with GridSearchCV and saves evaluation metrics to CSV."""
    df = load_data()

    # Save original indices before vectorization
    df_indices = df.index

    X = df[["latitude", "longitude"]]
    y = df['y_house_price_unit_area']

    # Train-test split (preserve indices)
    X_train, X_test, y_train, y_test, train_idx, test_idx = train_test_split(
        X, y, df_indices, test_size=0.2, random_state=42
    )

    if grid_search:
        rf = RandomForestRegressor(random_state=42)
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 5, 10]
        }

        grid_search = GridSearchCV(rf, param_grid, cv=3, scoring='accuracy', n_jobs=-1, verbose=1)
        grid_search.fit(X_train, y_train)

        best_model = grid_search.best_estimator_
        y_pred = best_model.predict(X_test)
    
    else:
        rf = RandomForestRegressor()
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)

    # salviamo il modello
    with open(os.path.join(config.MODELS_PATH, "random_forest_lat_long.pickle"), "wb") as file:
        pickle.dump(rf, file)

    # Create a DataFrame for the test set with predictions
    test_df = df.loc[test_idx].copy()  # Copy test set rows
    test_df['prediction'] = y_pred  # Add predictions


    # Compute metrics
    metrics = {
        'accuracy': mean_absolute_error(y_test, y_pred),
        "r2": r2_score(y_test, y_pred)
    }

    # Connect to the database
    conn = sqlite3.connect(config.DATABASE_PATH)

    # saving predictions
    test_df.to_sql(config.PREDICTIONS_TABLE, conn, if_exists='replace', index=False)
    
    # saving grid search results
    metrics_df = pd.DataFrame([metrics])
    metrics_df.to_sql(config.EVALUATION_TABLE, conn,
                      if_exists='replace', index=False)
    # Commit and close the connection
    conn.commit()
    conn.close()