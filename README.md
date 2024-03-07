# Women Safety Prediction Model

This repository contains a Python script for predicting women safety based on certain features of an area. The script utilizes a pre-trained machine learning model to make predictions.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python (version 3.x)
- Required Python libraries: numpy, json (install via `pip install numpy json`)

## Usage

To use the prediction model, you can call the `predict_safety` function with the name of the area as input. This function will return a prediction indicating the safety level of that area for women.

```python
from predict_model import predict_safety

# Example usage
area_name = "Area_Name"
safety_prediction = predict_safety(area_name)
print("Predicted Safety Level:", safety_prediction)
