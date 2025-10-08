import pandas as pd

# Path to your Excel file
excel_path = r"C:\Users\aravi\OneDrive\Desktop\RoadAccidentSeverityPrediction\data\accident_prediction_india.xlsx"

# Load the Excel file
df = pd.read_excel(excel_path)

# Save as CSV
csv_path = r"C:\Users\aravi\OneDrive\Desktop\RoadAccidentSeverityPrediction\data\accident_prediction_india.csv"
df.to_csv(csv_path, index=False)

print("Excel file has been converted to CSV!")
