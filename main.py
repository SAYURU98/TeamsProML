import os
import pandas as pd
from fastapi import FastAPI, UploadFile, File
import numpy as np
from posture_detection_functions import save_temp_file, extract_video_features, preprocess_features, predict_class
from joblib import load


from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_player_composition = load('model_RF with GridSearch - team composition.joblib')
model_strike_rates = load('model_RF with GridSearch - strike rates.joblib')
loaded_model = load('6 features_updated.joblib')

class_names = {
    0: 'correct_defence',
    1: 'correct_drive',
    2: 'wrong_defence',
    3: 'wrong_drive',
}

@app.post("/predictPosture")
async def predict(file: UploadFile = File(...)):
    try:
        temp_file_name = await save_temp_file(file)
        video_features = extract_video_features(temp_file_name)
        features = preprocess_features(video_features)
        predictions = predict_class(features)
        #predicted_class = np.argmax(predictions, axis=1)
        avg_prediction = np.mean(predictions, axis=0)
        # Get the class with the highest probability
        predicted_class = np.argmax(avg_prediction)
        predicted_class = class_names[predicted_class]
        os.remove(temp_file_name)
        return {'The predicted class is:': predicted_class}
    except Exception as e:
        return {'Error': str(e)}

@app.get("/team_composition")
async def predict_team_composition(team1: int, team2: int, winner: int, ground: int, margin_wickets: int, margin_runs: int, weather: int, toss: int, toss_decision: int):
    try:
        input_data = [team1, team2, winner, ground, margin_wickets, margin_runs,weather, toss, toss_decision]
        input_data = np.array(input_data).reshape(1, -1)
        prediction_player_composition = model_player_composition.predict(input_data)
        prediction_player_composition = prediction_player_composition.round().astype(int)
        prediction_strike_rates = np.round(model_player_composition.predict(input_data) * 10, 2)
        return {"team_composition": prediction_player_composition.tolist(),
                "strike_rates": prediction_strike_rates.tolist()}
    except Exception as e:
        return {"Error": str(e)}


@app.get('/nutrition_plan')
async def nutrition_plan(player_value: int, weight_in_kg: float, height_in_cm: float, blood_group: int, injury_type: int):
    try:
        new_data = pd.DataFrame([{'player_value': player_value, 'weight_in_kg': weight_in_kg, 'height_in_cm': height_in_cm, 'Blood_Type': blood_group, 'injury_type': injury_type}])
        new_pred = np.round(loaded_model.predict(new_data),3)
        return {"nutrition": new_pred.tolist()}
    except Exception as e:
        return {"Error": str(e)}