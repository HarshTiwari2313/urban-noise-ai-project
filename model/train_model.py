import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,r2_score
import pickle


# Load Data Set
df = pd.read_csv("E:\\urban_noise_ai_project\\data\\cleaned_noise_data.csv")

# Input features (X)
X = df.drop(columns=["Day", "Night"])

# Output (y) → multi-output
y = df[["Day", "Night"]]


# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# initialize Model
model = RandomForestRegressor()

model.fit(X_train,y_train)

print("Model Trained Successfully")


# Prediction

y_pred = model.predict(X_test)


#Evaluation

mae = mean_absolute_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print("MAE:", mae)
print("R2 Score:", r2)


pickle.dump(model, open("model.pkl", "wb"))


