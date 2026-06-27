import psycopg2
import pandas as pd

print("🚀 Loading data into PostgreSQL...")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="weather_db",
    user="airflow",
    password="airflow",
    port=5432
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id SERIAL PRIMARY KEY,
    date DATE,
    time_only TIME,
    temperature_celsius FLOAT,
    humidity_percent INT,
    wind_speed_kmh FLOAT
)
""")

conn.commit()

# Read transformed CSV
df = pd.read_csv("data/weather_transformed.csv")

# Insert data
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO weather
        (date, time_only, temperature_celsius,
         humidity_percent, wind_speed_kmh)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            row["date"],
            row["time_only"],
            row["temperature_celsius"],
            row["humidity_percent"],
            row["wind_speed_kmh"],
        ),
    )

conn.commit()

print("✅ Data Loaded Successfully!")

cursor.close()
conn.close()