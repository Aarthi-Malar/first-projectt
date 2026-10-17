
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("flood_risk_dataset.csv")

# Display dataset
print("Dataset Preview:")
print(data.head())
print("\nDataset Columns:")
print(data.columns.tolist())

# Separate input and target
# Dataset columns-ai verify pannitu
# keezha correct column names use pannanum.
