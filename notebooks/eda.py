import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/traffic_data.csv")

print("Shape:", df.shape)
print(df.info())
print(df.describe())

print("\nMissing values:\n", df.isnull().sum())

df['congestion_level'] = df['congestion_level'].str.strip()
df['weather'] = df['weather'].str.strip()
# [1] Traffic Level Count
colors = ['#2ecc71', '#f1c40f', '#e74c3c']  

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

# [2] Weather Impact
plt.figure(figsize=(8,5))

colors = ['#3498db', '#9b59b6', '#1abc9c']  

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

# [3] Feature Correlation Analysis
plt.figure(figsize=(8,6))
corr = df[['vehicle_count','avg_speed','signal_delay','is_peak_hour','accident_reported']].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    linewidths=1,
    linecolor='black'
)
plt.title("Feature Correlation Heatmap", fontsize=14, fontweight='bold')
plt.show() 

# [4] Vehicle Count vs Speed by Congestion Level
colors_map = {'low':'#2ecc71', 'medium':'#f1c40f', 'high':'#e74c3c'}
plt.figure(figsize=(7,5))
for level in df['congestion_level'].unique():
    subset = df[df['congestion_level'] == level]
    plt.scatter(
        subset['vehicle_count'],
        subset['avg_speed'],
        label=level,
        color=colors_map[level],
        s=80,
        edgecolors='black'
    )



