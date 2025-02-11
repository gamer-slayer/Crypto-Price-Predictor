import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('crypto_price_model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Get JSON data from request
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)  # Predict price
        return jsonify({'prediction': float(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
