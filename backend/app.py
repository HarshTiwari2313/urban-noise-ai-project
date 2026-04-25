from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# Station Mapping
station_map = {
    "BEN01": 0, "BEN02": 1, "BEN03": 2, "BEN04": 3, "BEN05": 4,
    "CHE01": 5, "CHE02": 6, "CHE03": 7, "CHE04": 8, "CHE05": 9,
    "DEL01": 10, "DEL02": 11, "DEL03": 12, "DEL04": 13, "DEL05": 14,
    "HYD01": 15, "HYD02": 16, "HYD03": 17, "HYD04": 18, "HYD05": 19,
    "KOL01": 20, "KOL02": 21, "KOL03": 22, "KOL04": 23, "KOL05": 24,
    "LUC01": 25, "LUC02": 26, "LUC03": 27, "LUC04": 28, "LUC05": 29,
    "MUM01": 30, "MUM02": 31, "MUM03": 32, "MUM04": 33, "MUM05": 34,

    "BEN06": 35, "BEN07": 36, "BEN08": 37, "BEN09": 38, "BEN10": 39,
    "CHE06": 40, "CHE07": 41, "CHE08": 42, "CHE09": 43, "CHE10": 44,
    "DEL06": 45, "DEL07": 46, "DEL08": 47, "DEL09": 48, "DEL10": 49,
    "HYD06": 50, "HYD07": 51, "HYD08": 52, "HYD09": 53, "HYD10": 54,
    "KOL06": 55, "KOL07": 56, "KOL08": 57, "KOL09": 58, "KOL10": 59,
    "LUC06": 60, "LUC07": 61, "LUC08": 62, "LUC09": 63, "LUC10": 64,
    "MUM06": 65, "MUM07": 66, "MUM08": 67, "MUM09": 68, "MUM10": 69
}

# Home route
@app.route("/")
def home():
    return "Backend Running Successfully........."

# Load model
model = pickle.load(open("E:\\urban_noise_ai_project\\model.pkl", "rb"))

# Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        # ✅ Convert station name → number
        station_name = data["Station"]
        station = station_map[station_name]

        features = [
            station,
            data["Year"],
            data["Month"],
            55,   # fixed DayLimit
            45    # fixed NightLimit
        ]

        features = np.array([features])

        prediction = model.predict(features)

        return jsonify({
            "Day": float(prediction[0][0]),
            "Night": float(prediction[0][1])
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)