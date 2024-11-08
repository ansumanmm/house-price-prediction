import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the model and column names
with open('Housing_Model.pkl', 'rb') as file:
    data = pickle.load(file)
    model = data['model']  # Extract the trained model
    expected_columns = data['columns']  # Extract the expected column names

@app.route('/')
def index():
    # Serve the HTML form from templates
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form submission
    input_data = request.json

    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # One-hot encode categorical variables
    input_df = pd.get_dummies(input_df, columns=['mainroad', 'guestroom', 'basement',
                                                 'hotwaterheating', 'airconditioning',
                                                 'prefarea', 'furnishingstatus'], drop_first=True)

    # Ensure the input data has the same features as the model's expected features
    missing_cols = set(expected_columns) - set(input_df.columns)
    for col in missing_cols:
        input_df[col] = 0  # Add missing columns with default value 0

    # Drop any extra columns that aren't part of the expected columns
    input_df = input_df[expected_columns]

    # Predict the price using the trained model
    prediction = model.predict(input_df)

    # Return the prediction as JSON
    return jsonify({'predicted_price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
