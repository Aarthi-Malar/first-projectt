
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the dataset from the project folder
file_path = Path(__file__).parent / "flood_risk_dataset.csv"
df = pd.read_csv(file_path)

# 1. Basic dataset information
print("\n--- Dataset Preview ---")
print(df.head())

print("\n--- Dataset Shape ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n--- Column Names ---")
print(df.columns.tolist())

# 2. Data types and missing values
print("\n--- Dataset Information ---")
df.info()

print("\n--- Missing Values ---")
print(df.isnull().sum())

# 3. Statistical summary
print("\n--- Statistical Summary ---")
print(df.describe())

# 4. Target class distribution
if "Flood" in df.columns:
    print("\n--- Flood Class Distribution ---")
    print(df["Flood"].value_counts())

    df["Flood"].value_counts().sort_index().plot(
        kind="bar",
        title="Flood Class Distribution",
        xlabel="Flood Class",
        ylabel="Number of Records"
    )
    plt.tight_layout()
    plt.savefig("flood_class_distribution.png")
    plt.show()

# 5. Feature distributions
columns_to_plot = [
    "Rainfall_mm",
    "River_Level_m",
    "Humidity_percent",
    "Temperature_C"
]

available_columns = [
    col for col in columns_to_plot if col in df.columns
]

if available_columns:
    df[available_columns].hist(figsize=(10, 7), bins=10)
    plt.suptitle("Environmental Feature Distributions")
    plt.tight_layout()
    plt.savefig("feature_distributions.png")
    plt.show()

print("\nData analysis completed!")
