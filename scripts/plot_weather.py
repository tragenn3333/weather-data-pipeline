import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

conn = psycopg2.connect(
    host="localhost", database="weather_db",
    user="airflow", password="airflow", port=5432
)
df = pd.read_sql("SELECT * FROM weather ORDER BY id", conn)
conn.close()

df["datetime"] = pd.to_datetime(df["date"].astype(str) + " " + df["time_only"].astype(str))

fig, axs = plt.subplots(3, 1, figsize=(8, 10))
axs[0].plot(df["datetime"], df["temperature_celsius"], marker="o", color="red")
axs[0].set_title("Temperature (°C)")

axs[1].plot(df["datetime"], df["humidity_percent"], marker="o", color="blue")
axs[1].set_title("Humidity (%)")

axs[2].plot(df["datetime"], df["wind_speed_kmh"], marker="o", color="green")
axs[2].set_title("Wind Speed (km/h)")

plt.tight_layout()
plt.savefig("data/weather_chart.png")
print("✅ Chart saved to data/weather_chart.png")