import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load your dataset
data = pd.read_csv('dataset.csv')

# Print the column names for debugging
print("Columns in dataset before preprocessing:", data.columns.tolist())

# Check if 'price' is in the dataset
if 'price' not in data.columns:
    raise KeyError("Column 'price' not found in the dataset.")

# One-hot encode categorical variables
data = pd.get_dummies(data, columns=['mainroad', 'guestroom', 'basement',
                                      'hotwaterheating', 'airconditioning',
                                      'parking', 'prefarea', 'furnishingstatus'], drop_first=True)

# Print the shape of the data after preprocessing
print("Columns in dataset after preprocessing:", data.columns.tolist())
print("Shape of data after preprocessing:", data.shape)

# Define your features and target variable
X = data.drop('price', axis=1)  # Drop the target variable from features
y = data['price']  # Assuming 'price' is the target variable

# Print the shape of the features and target
print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train your model
model = LinearRegression()
model.fit(X_train, y_train)

# Print the number of features the model was trained on
print("Number of features the model was trained on:", X_train.shape[1])

# Save the model and the column names
with open('Housing_Model.pkl', 'wb') as file:
    pickle.dump({'model': model, 'columns': X_train.columns.tolist()}, file)

print("Model saved successfully!")
