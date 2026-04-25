import pandas as pd

# Load Data

df = pd.read_csv("E:\\urban_noise_ai_project\\data\\cleaned_noise_data.csv")
print("Data Frame Loaded.....")
print(df.head())


#Kaunse month me noise zyada hota hai?
print("\n Average Day Noise By Month:")
month_avg = df.groupby("Month")["Day"].mean()

print(month_avg)



#Kaun sa Station (area) sabse zyada noisy hai?
print("\nAverage Day Noise by Station:")

station_avg = df.groupby("Station")["Day"].mean()
print(station_avg)



#Noise Limit Exceed Analysis->Kitni baar noise allowed limit cross kar raha hai
df["Exceed"] = df["Day"] > df["DayLimit"]
print("\nNoise Limit Exceed Count:")
print(df["Exceed"].value_counts())

# Maximum Noise Level
print("\nMaximum Day Noise Level:")
print(df["Day"].max())