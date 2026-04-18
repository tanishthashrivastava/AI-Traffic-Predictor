# 1. Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 2. Load Dataset
df = pd.read_csv("data/traffic_data.csv")

# 3. Data Preprocessing
le = LabelEncoder()

df['location'] = le.fit_transform(df['location'])
df['traffic_density'] = le.fit_transform(df['traffic_density'])
df['road_type'] = le.fit_transform(df['road_type'])
df['weather'] = le.fit_transform(df['weather'])
df['congestion_level'] = le.fit_transform(df['congestion_level'])

# 4. Features & Target
X = df.drop(['congestion_level', 'timestamp'], axis=1)
y = df['congestion_level']

# 5. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 7. Prediction
y_pred = model.predict(X_test)

# 8. Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nReport:\n", classification_report(y_test, y_pred)) 



# SAVE MODEL
import joblib
joblib.dump(model, "models/traffic_model.pkl")
print("Model saved successfully!")