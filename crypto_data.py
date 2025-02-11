import requests
import pandas as pd

def fetch_crypto_data(crypto='bitcoin'):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "30",  # Last 30 days data
        "interval": "daily"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        prices = data['prices']
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    else:
        print("Error fetching data")
        return None

# Test fetching Bitcoin Data
if __name__ == "__main__":
    df = fetch_crypto_data()
    print(df.head())  
