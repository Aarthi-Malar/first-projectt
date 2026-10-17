
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the dataset
data = pd.read_csv("flood_risk_dataset.csv")

print("Dataset Preview:")
print(data.head())

# 2. Select input features and target
X = data[
    [
        "Rainfall_mm",
        "River_Level_m",
        "Humidity_percent",
        "Temperature_C"
    ]
]

y = data["Flood"]

# 3. Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# 4. Create the Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# 5. Train the model
model.fit(X_train, y_train)

# 6. Evaluate the model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Evaluation")
print("----------------")
print(f"Test Accuracy: {accuracy:.2%}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# 7. Predict for a new sample
new_data = pd.DataFrame([{
    "Rainfall_mm": 250,
    "River_Level_m": 8,
    "Humidity_percent": 90,
    "Temperature_C": 25
}])

prediction = model.predict(new_data)[0]
probability = model.predict_proba(new_data)[0][1]

print("\nNew Sample Prediction")
if prediction == 1:
    print("Predicted Flood Class: 1")
else:
    print("Predicted Flood Class: 0")

print(f"Model-estimated probability of class 1: {probability:.2%}")
print("\nNote: Educational demonstration only.")
