import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os


data_path = 'data/accident_prediction_india.xlsx'  


df = pd.read_csv(data_path, encoding='ISO-8859-1')
le_vehicle_type = LabelEncoder()
le_vehicle_type.fit(df['Vehicle Type Involved'])
if not os.path.exists('model'):
    os.makedirs('model')


joblib.dump(le_vehicle_type, 'model/le_vehicle_type.pkl')

print("LabelEncoder for 'Vehicle Type Involved' saved successfully!")
