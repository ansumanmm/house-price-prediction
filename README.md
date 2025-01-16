# Housing Price Prediction Web Application

This repository contains a Flask-based web application for predicting housing prices using a pre-trained machine learning model.

## Features
- Accepts user input through a web form.
- Processes input data to match the expected format of the trained model.
- Predicts housing prices and returns the result in JSON format.

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.x
- Flask
- pandas
- pickle (standard library in Python 3)

## Files in the Repository
- `app.py`: Main Flask application.
- `Housing_Model.pkl`: Pickle file containing the trained model and expected column names.
- `templates/index.html`: HTML file for the user interface.
- `README.md`: Documentation for the project.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required Python packages:
   ```bash
   pip install Flask pandas
   ```

3. Ensure the `Housing_Model.pkl` file is present in the project directory.

## Usage
1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`.

3. Enter housing details in the provided form and submit.

4. View the predicted price returned by the application.

## API Endpoint
### `/predict`
- **Method:** POST
- **Description:** Accepts housing data in JSON format and returns the predicted price.
- **Input Format:**
  ```json
  {
    "area": 1500,
    "bedrooms": 3,
    "bathrooms": 2,
    "stories": 2,
    "mainroad": "yes",
    "guestroom": "no",
    "basement": "no",
    "hotwaterheating": "no",
    "airconditioning": "yes",
    "parking": 1,
    "prefarea": "yes",
    "furnishingstatus": "furnished"
  }
  ```
- **Response Format:**
  ```json
  {
    "predicted_price": 123456.78
  }
  ```

## Notes
- The `Housing_Model.pkl` file contains both the trained model and the expected feature columns.
- The application ensures input data is aligned with the expected format by adding missing columns and dropping extra ones.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Thanks to the contributors and the open-source community for their support.
