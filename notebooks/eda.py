import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/traffic_data.csv")

print("Shape:", df.shape)
print(df.info())
print(df.describe())

print("\nMissing values:\n", df.isnull().sum())


# [1] Traffic Level Count
colors = ['#2ecc71', '#f1c40f', '#e74c3c']  # green, yellow, red

df['congestion_level'].value_counts().plot(
    kind='bar',
    color=colors,
    edgecolor='black'
)

plt.title("Traffic Congestion Distribution", fontsize=14, fontweight='bold')
plt.xlabel("Congestion Level")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show() 

# [2] Vehicle Count vs Congestion
plt.figure(figsize=(8,5))
plt.scatter(
    df['vehicle_count'],
    df['avg_speed'],
    color='#3498db',        
    edgecolor='black',
    alpha=0.7
)

plt.title("Vehicle Count vs Speed", fontsize=14, fontweight='bold')
plt.xlabel("Vehicle Count")
plt.ylabel("Average Speed")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()  

# [3] Weather Impact
plt.figure(figsize=(8,5))

colors = ['#3498db', '#9b59b6', '#1abc9c']  # blue, purple, teal

df.groupby('weather')['vehicle_count'].mean().plot(
    kind='bar',
    color=colors,
    edgecolor='black'
)

plt.title("Weather Impact on Traffic", fontsize=14, fontweight='bold')
plt.xlabel("Weather Condition")
plt.ylabel("Average Vehicle Count")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# [4] Peak Hour Effect
plt.figure(figsize=(8,5))

color_map = {
    0: '#2ecc71',   # Non-peak → green
    1: '#e74c3c'    # Peak → red
}

peak_avg = df.groupby('is_peak_hour')['vehicle_count'].mean()
colors = [color_map[i] for i in peak_avg.index]

peak_avg.plot(
    kind='bar',
    color=colors,
    edgecolor='black'
)
plt.title("Peak Hour vs Traffic", fontsize=14, fontweight='bold')
plt.xlabel("Is Peak Hour (0 = No, 1 = Yes)")
plt.ylabel("Average Vehicle Count")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show() 