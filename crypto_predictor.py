import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from crypto_data import fetch_crypto_data

def train_model():
    df = fetch_crypto_data('bitcoin')

    df['target'] = df['price'].shift(-1)  # Next day's price as target
    df.dropna(inplace=True)  

    X = df[['price']]  
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

# Test the model
if __name__ == "__main__":
    model = train_model()
    print("Model trained successfully!")
