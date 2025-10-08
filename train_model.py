import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import os


df = pd.read_csv("data/accident_prediction_india.csv")

df.dropna(inplace=True)

label_encoders = {}
categorical_columns = [
    'Day of Week', 'Vehicle Type Involved', 'Weather Conditions',
    'Road Type', 'Road Condition', 'Lighting Conditions',
    'Driver Gender', 'Alcohol Involvement'
]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le
    joblib.dump(le, f"model/le_{col.lower().replace(' ', '_')}.pkl")


le_target = LabelEncoder()
df['Accident Severity'] = le_target.fit_transform(df['Accident Severity'])
joblib.dump(le_target, "model/le_accident_severity.pkl")

features = [
    'Day of Week', 'Vehicle Type Involved', 'Weather Conditions',
    'Road Type', 'Road Condition', 'Lighting Conditions',
    'Speed Limit (km/h)', 'Driver Age', 'Driver Gender', 'Alcohol Involvement'
]
X = df[features]
y = df['Accident Severity']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "model/model.pkl")

print("Model and encoders saved!")

joblib.dump(le_vehicle_type, 'model/le_vehicle_type.pkl')
joblib.dump(le_weather, 'model/le_weather.pkl')
joblib.dump(le_road_type, 'model/le_road_type.pkl')

encoders = {
    "Vehicle Type Involved": le_vehicle_type,
    "Weather Conditions": le_weather,
    "Road Type": le_road_type,
    "Road Condition": le_road_condition,
    "Lighting Conditions": le_lighting,
    "Driver Gender": le_gender,
    "Alcohol Involvement": le_alcohol,
    "Day of Week": le_day,
    "State Name": le_state,
    "City Name": le_city
}

for field, le in encoders.items():
    print(f"{field}:", list(le.classes_))
