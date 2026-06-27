import pandas as pd

print("🚀 Weather Data Transformation Started")

# Read extracted weather data
df = pd.read_csv("data/weather_data.csv")

print("\nOriginal Data:")
print(df)

# Convert time column to datetime
df["time"] = pd.to_datetime(df["time"])

# Create date and time columns
df["date"] = df["time"].dt.date
df["time_only"] = df["time"].dt.time

# Rename columns
df.rename(columns={
    "temperature": "temperature_celsius",
    "humidity": "humidity_percent",
    "wind_speed": "wind_speed_kmh"
}, inplace=True)

# Select columns in required order
df = df[
    [
        "date",
        "time_only",
        "temperature_celsius",
        "humidity_percent",
        "wind_speed_kmh"
    ]
]

print("\nTransformed Data:")
print(df)

# Save transformed file
df.to_csv("data/weather_transformed.csv", index=False)

print("\n✅ Transformation Completed Successfully!")
print("File saved as data/weather_transformed.csv")