
# 🌊 Flood Risk Prediction using Machine Learning

A beginner-friendly Machine Learning project that
explores flood-related classification using weather
and environmental data.

## 📌 Project Overview

Flooding can cause serious damage to people,
property, and the environment. This project
demonstrates a basic Machine Learning workflow
for classifying flood-related outcomes from
selected environmental features.

The model uses a Random Forest Classifier
implemented with Python and Scikit-learn.

> Educational project only. This model is not
> designed for real-world flood warnings.

## 🎯 Objectives

- Understand a real-world Machine Learning use case.
- Explore environmental data using Pandas.
- Train a Random Forest classification model.
- Evaluate predictions using classification metrics.
- Learn how to organize and document a GitHub project.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Random Forest Classifier
- GitHub

## 📊 Dataset Description

The dataset contains the following features:

| Feature | Description |
|---|---|
| Rainfall_mm | Rainfall measurement in mm |
| River_Level_m | River level measurement in metres |
| Humidity_percent | Humidity percentage |
| Temperature_C | Temperature in Celsius |
| Flood | Target class supplied in the dataset |

The target values are used as provided in the
dataset. Their real-world interpretation must be
verified before practical use.

## ⚙️ Machine Learning Workflow

1. Load the CSV dataset.
2. Inspect the dataset and its features.
3. Separate input features and target labels.
4. Split data into training and testing sets.
5. Train a Random Forest Classifier.
6. Evaluate the model on test data.
7. Generate a prediction for a new sample.

## 📈 Initial Model Evaluation

The current test split produced 95% accuracy
on 20 test samples.

This is an initial result from a small dataset.
It does not establish generalization to unseen
locations, weather conditions, or future floods.

Additional validation is needed before drawing
reliable conclusions.

## 🚀 Getting Started

### Prerequisites

- Python 3
- pip

### Installation

Clone or download this repository, then open
a terminal in the project folder.

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the model:

```bash
python main.py
```

## 📁 Project Structure

```text
first-projectt/
├── main.py
├── flood_risk_dataset.csv
├── requirements.txt
└── README.md
```

## 🔮 Future Improvements

- Add exploratory data analysis and visualizations.
- Compare multiple classification algorithms.
- Include a confusion matrix and F1-score.
- Validate the model using more reliable data.
- Build an interactive prediction dashboard.

## 👩‍💻 Author

Aarthi M

## ⚠️ Disclaimer

This project is for educational purposes only.
Predictions must not be used for emergency
response or real-world flood safety decisions.
