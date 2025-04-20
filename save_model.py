import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import os

# Load dataset
df = pd.read_csv("day.csv")
df = df.drop(['instant', 'dteday', 'casual', 'registered'], axis=1)
df.rename(columns={'cnt': 'total_rentals'}, inplace=True)

# Features and target
X = df[['temp', 'hum', 'windspeed']]
y = df['total_rentals']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Ensure 'model/' directory exists
os.makedirs("model", exist_ok=True)

# Save model
with open('model/rental_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Model trained and saved to 'model/rental_model.pkl'.")
