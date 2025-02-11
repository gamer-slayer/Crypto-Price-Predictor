import streamlit as st
from crypto_predictor import train_model, fetch_crypto_data

st.title("Crypto Price Predictor 🚀")

crypto = st.selectbox("Choose Cryptocurrency", ["bitcoin", "ethereum"])

df = fetch_crypto_data(crypto)

st.subheader(f"Last 30 Days {crypto.capitalize()} Prices")
st.line_chart(df.set_index("timestamp")["price"])

model = train_model()
latest_price = df['price'].iloc[-1]

predicted_price = model.predict([[latest_price]])[0]

st.subheader(f"Prediction for Next Day: ${predicted_price:.2f}")
