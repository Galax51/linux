from fastapi import FastAPI
from models import HouseFeatures
from predictor import predict_price
from dekorator import log_function_args_and_output
app = FastAPI()
# Load the model (make sure this path is correct)
@app.post("/predict")
@log_function_args_and_output
def predict(features: HouseFeatures):
    predicted_price = predict_price(features)
    return {"predicted_price": predicted_price}

