## Project Overview

This project focuses on building a Hybrid Predictive Traffic Intelligence System that analyzes and forecasts traffic congestion using AI/ML techniques. 

The system integrates vehicle density analysis (via computer vision) and historical traffic data to predict congestion hotspots in advance. The goal is to move from reactive traffic monitoring to proactive traffic prediction, improving urban mobility and decision-making.

## Problem Statement

Current traffic systems are reactive and fail to provide insights into future congestion patterns. This project addresses this gap by developing a predictive model that can estimate traffic conditions 15–45 minutes in advance.

## Objectives

- Analyze traffic patterns using historical data
- Estimate vehicle density using computer vision (YOLO - optional)
- Predict future congestion using machine learning models
- Visualize traffic hotspots on an interactive dashboard

## Tech Stack

- Python (Pandas, NumPy)
- Machine Learning (Scikit-learn / LSTM)
- OpenCV (for vehicle detection - optional)
- Streamlit (for dashboard visualization)
- Git & GitHub (version control) 

## Exploratory Data Analysis (EDA)

To understand traffic patterns, several visualizations were created:

### 1. Traffic Congestion Distribution
This bar chart shows the frequency of low, medium, and high congestion levels. It helps identify how often traffic congestion occurs under different conditions.

### 2. Weather Impact on Traffic
This visualization highlights how weather conditions (clear, rain, fog) affect vehicle density. It was observed that adverse weather conditions increase traffic congestion.

### 3. Feature Correlation Heatmap
A heatmap was used to analyze relationships between numerical features such as vehicle count, speed, signal delay, and peak hours. Strong correlations help in selecting important features for model building.

### 4. Traffic Pattern Analysis (Vehicle Count vs Speed)
This scatter plot, colored by congestion level, shows that higher vehicle count leads to lower speed, indicating higher congestion. This visualization provides clear insight into traffic dynamics.

## Key Insights
- Traffic congestion increases significantly during high vehicle count
- Weather conditions like rain and fog contribute to higher congestion
- Speed is inversely related to traffic density
- Signal delays and accidents impact congestion levels