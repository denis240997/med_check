# imports
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import numpy as np
import pandas as pd
import tensorflow as tf


# open pretrained network and compile
with open('risk_prediction/ml_model/data/model.json', 'r') as json_file:
    json_file = json_file.read() 

model = tf.keras.models.model_from_json(json_file)
model.load_weights('risk_prediction/ml_model/data/model.h5')
model.compile(optimizer='Adam', loss='mse', metrics=['accuracy'])

def convert_factor_names(factors_py):
    NAMES_MAP = {
        'heart_rate': 'heartRate',
        'is_smoking': 'currentSmoker',
        'cigarets_per_day': 'cigsPerDay',
        'blood_pressure_medicines': 'BPMeds',
        'stroke': 'prevalentStroke',
        'hypertension': 'prevalentHyp',
        'systolic_blood_pressure': 'sysBP',
        'diastolic_blood_pressure': 'diaBP',
    }
    factors = factors_py.copy()
    for key in NAMES_MAP:
        value = factors[key]
        del factors[key]
        factors[NAMES_MAP[key]] = value
        
    factors['male'] = True if factors['gender'] == 'M' else False
    del factors['gender']
    
    factors['BMI'] = factors['weight'] / factors['height']**2
    del factors['weight']
    del factors['height']

    for key, val in factors.items():
        if type(val) == bool:
            factors[key] = int(val)
        
    return factors

columns = ['male',
    'age',
    'currentSmoker',
    'cigsPerDay',
    'BPMeds',
    'prevalentStroke',
    'prevalentHyp',
    'diabetes',
    'sysBP',
    'diaBP',
    'BMI',
    'heartRate'
 ]
df = pd.DataFrame(columns=columns)

# function to receive an input and make inference
def predict_risk(input_data):
    data = convert_factor_names(input_data)
    return float(model.predict(df.append(data, ignore_index=True)).clip(0, 1) * 100)

if __name__ == '__main__':
    test_data = {
        'gender': 'M',
        'age': 33,
        'height': 1.78,
        'weight': 90,
        'heart_rate': 80,
        'is_smoking': True,
        'cigarets_per_day': 5,
        'blood_pressure_medicines': False,
        'stroke': False,
        'hypertension': True,
        'diabetes': False,
        'systolic_blood_pressure': 120,
        'diastolic_blood_pressure': 70,
    }
    print(predict_risk(test_data))
    