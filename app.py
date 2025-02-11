import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

try:
    model = pickle.load(open('crypto_price_model.pkl', 'rb'))
except Exception as e:
    print("Error loading model:", str(e))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({'prediction': float(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
