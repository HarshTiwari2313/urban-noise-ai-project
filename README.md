# 🌆 Urban Noise Level Prediction System

## 📌 Project Overview

This project predicts urban noise levels (Day & Night) using environmental data such as location, year, and month. It also analyzes noise pollution trends and classifies noise levels into Safe, Moderate, and High categories.

---

## 🚀 Features

* 🔍 Noise Prediction (Day & Night)
* 📊 Noise Classification (Safe / Moderate / High)
* 🧠 Machine Learning Model (Random Forest)
* 🌐 Full Stack Application (React + Flask)
* 📁 Real-world Dataset (India Noise Monitoring Data)

---

## 🧠 Tech Stack

* Python (Pandas, NumPy, Scikit-learn)
* Flask (Backend API)
* React.js (Frontend UI)
* Machine Learning (Random Forest Regressor)

---

## 📊 Dataset

* Source: Kaggle
* Name: Noise Monitoring Data in India (2011–2018)

---

## ⚙️ How It Works

1. User selects:

   * Station
   * Year
   * Month
2. Frontend sends data to Flask API
3. Backend loads trained ML model
4. Model predicts:

   * Day Noise
   * Night Noise
5. Output is displayed with noise classification

---

## 📈 Model Performance

| Metric   | Value |
| -------- | ----- |
| MAE      | ~1.84 |
| R² Score | ~0.80 |

---

## 🔍 Analysis

* Noise remains relatively stable across months
* Significant variation across locations
* ~72% cases exceed safe noise limits
* Maximum recorded noise: 100 dB

---

## 📁 Project Structure

```
urban_noise_ai_project/
│
├── backend/        # Flask API  
├── frontend/       # React UI  
├── model/          # ML training code  
├── data/           # Dataset  
├── model.pkl       # Trained model  
└── README.md  
```

---

## 🚀 Run Locally

### Backend

```
cd backend
python app.py
```

### Frontend

```
cd frontend
npm install
npm start
```

---

## 🔮 Future Improvements

* 📊 Graph Visualization
* 🌐 Live Deployment
* 📡 Real-time Noise Monitoring

---

## 👨‍💻 Author

**Harsh Tiwari**
© 2026 All Rights Reserved

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
