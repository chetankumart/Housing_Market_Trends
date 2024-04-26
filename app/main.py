from flask import Flask, request, render_template
import joblib
import numpy as np

model = joblib.load('./model/rf_model.pkl')
# scaler = joblib.load('path_to_scaler/scaler.pkl')
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features = np.array(input_features).reshape(1, -1)
    prediction = model.predict(features)
    return render_template('index.html', prediction_text=f'Estimated House Price: ${prediction[0]:,.2f}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
