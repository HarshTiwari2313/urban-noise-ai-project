import pandas as pd

# Load dataset
df = pd.read_csv("E:\\urban_noise_ai_project\\data\\noise_data.csv")

# print("Data Loaded:")
# print(df.head())


print("Total Uniques:", df['Station'].unique())

# Convert Station to numeric
df["Station"] = df["Station"].astype("category").cat.codes


# print("\nAfter Encoding:")
# print(df.head())


# Checking Null Value

# print("\nMissing Values:\n")
# print(df.isnull().sum())


# Drop Null Value
df = df.dropna()

# print("\nAfter removing null values:")
# print(df.isnull().sum())

# print("\nMissing Values:\n")
# print(df.isnull().sum())


# Export Clean Data

df.to_csv("E:\\urban_noise_ai_project\\data\\cleaned_noise_data.csv", index=False)

print("Cleaned data saved successfully")
