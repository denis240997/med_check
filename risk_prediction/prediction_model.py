import random
import pandas as pd

# {
#   "male" : "0",
#   "age" : "67",
#   "currentSmoker": "0",
#   "cigsPerDay": "0",
#   "BPMeds": "1",
#   "prevalentStroke": "0",
#   "prevalentHyp": "0",
#   "diabetes": "0",
#   "sysBP": "106.0",
#   "diaBP": "70.0",
#   "BMI": "29.97",
#   "heartRate": "80.0"
# }

def predict_risk(data):
    model_input = pd.Series(data)
    return f'{random.random()*100:.1f}'