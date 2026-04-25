import React, { useState } from "react";
import "./App.css";

function App() {

  const stations = [
    "BEN01","BEN02","BEN03","BEN04","BEN05",
    "CHE01","CHE02","CHE03","CHE04","CHE05",
    "DEL01","DEL02","DEL03","DEL04","DEL05",
    "HYD01","HYD02","HYD03","HYD04","HYD05",
    "KOL01","KOL02","KOL03","KOL04","KOL05",
    "LUC01","LUC02","LUC03","LUC04","LUC05",
    "MUM01","MUM02","MUM03","MUM04","MUM05",

    "BEN06","BEN07","BEN08","BEN09","BEN10",
    "CHE06","CHE07","CHE08","CHE09","CHE10",
    "DEL06","DEL07","DEL08","DEL09","DEL10",
    "HYD06","HYD07","HYD08","HYD09","HYD10",
    "KOL06","KOL07","KOL08","KOL09","KOL10",
    "LUC06","LUC07","LUC08","LUC09","LUC10",
    "MUM06","MUM07","MUM08","MUM09","MUM10"
  ];

  const [form, setForm] = useState({
    Station: "",
    Year: "",
    Month: ""
  });

  const [result, setResult] = useState(null);

const handleChange = (e) => {
  setForm({ ...form, [e.target.name]: e.target.value });
  setResult(null); // 🔥 ye line add karo
};
  const predict = async () => {

    // ✅ Validation
    if (!form.Station || !form.Year || !form.Month) {
      alert("Please fill all fields ❌");
      return;
    }

    try {
      const res = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          Station: form.Station,
          Year: Number(form.Year),
          Month: Number(form.Month)
        })
      });

      const data = await res.json();
      setResult(data);

    } catch (error) {
      alert("Backend not running ❌");
    }
  };

  return (
    <div className="container">
      <h1>🌆 Urban Noise Predictor</h1>

      <div className="card">

        {/* 🔽 Station Dropdown */}
        <select name="Station" onChange={handleChange}>
          <option value="">Select Station</option>
          {stations.map((s) => (
            <option key={s} value={s}>{s}</option>
          ))}
        </select>

        <input name="Year" placeholder="Year" onChange={handleChange} />
        <input name="Month" placeholder="Month (1-12)" onChange={handleChange} />

        <button onClick={predict}>Predict</button>
      </div>

      {result && (
        <div className="result">
          <h2>📊 Prediction Result</h2>

          <p>🌞 Day Noise: <b>{result.Day.toFixed(2)} dB</b></p>
          <p>🌙 Night Noise: <b>{result.Night.toFixed(2)} dB</b></p>

          {/* 🔥 Smart Noise Level Classification */}
          {result.Day > 75 || result.Night > 65 ? (
            <p style={{ color: "red", fontWeight: "bold" }}>
              🚨 Very High Noise!
            </p>
          ) : result.Day > 60 || result.Night > 50 ? (
            <p style={{ color: "orange", fontWeight: "bold" }}>
              ⚠️ Moderate Noise
            </p>
          ) : (
            <p style={{ color: "green", fontWeight: "bold" }}>
              ✅ Noise Level Safe
            </p>
          )}
        </div>
      )}
      <footer className="footer">
  © 2026 Harsh Tiwari. All Rights Reserved.
</footer>
    </div>
  );
}

export default App;