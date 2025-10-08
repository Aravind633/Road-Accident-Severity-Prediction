# from flask import Flask, render_template, request
# import joblib

# app = Flask(__name__)

# model = joblib.load("model/model.pkl")

# # Load label encoders
# encoders = {
#     'Day of Week': joblib.load("model/le_day_of_week.pkl"),
#     'Vehicle Type Involved': joblib.load("model/le_vehicle_type_involved.pkl"),
#     'Weather Conditions': joblib.load("model/le_weather_conditions.pkl"),
#     'Road Type': joblib.load("model/le_road_type.pkl"),
#     'Road Condition': joblib.load("model/le_road_condition.pkl"),
#     'Lighting Conditions': joblib.load("model/le_lighting_conditions.pkl"),
#     'Driver Gender': joblib.load("model/le_driver_gender.pkl"),
#     'Alcohol Involvement': joblib.load("model/le_alcohol_involvement.pkl"),
# }
# target_encoder = joblib.load("model/le_accident_severity.pkl")

# @app.route('/')
# def index():
#     # Create a dictionary of options extracted from LabelEncoders
#     dropdown_options = {key: list(encoder.classes_) for key, encoder in encoders.items()}
#     return render_template("index.html", options=dropdown_options)

# @app.route('/predict', methods=['POST'])
# def predict():
#     input_data = {
#         'Day of Week': request.form['day_of_week'],
#         'Vehicle Type Involved': request.form['vehicle_type'],
#         'Weather Conditions': request.form['weather'],
#         'Road Type': request.form['road_type'],
#         'Road Condition': request.form['road_condition'],
#         'Lighting Conditions': request.form['lighting'],
#         'Speed Limit (km/h)': int(request.form['speed']),
#         'Driver Age': int(request.form['age']),
#         'Driver Gender': request.form['gender'],
#         'Alcohol Involvement': request.form['alcohol']
#     }

#     # Encode input
#     encoded = []
#     for key in input_data:
#         if key in encoders:
#             encoded.append(encoders[key].transform([input_data[key]])[0])
#         else:
#             encoded.append(input_data[key])

#     pred = model.predict([encoded])[0]
#     severity = target_encoder.inverse_transform([pred])[0]

#     # Also pass dropdown options here again for form rendering
#     dropdown_options = {key: list(encoder.classes_) for key, encoder in encoders.items()}
#     return render_template("index.html", prediction=severity, options=dropdown_options)

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model/model.pkl")

encoders = {
    'Day of Week': joblib.load("model/le_day_of_week.pkl"),
    'Vehicle Type Involved': joblib.load("model/le_vehicle_type_involved.pkl"),
    'Weather Conditions': joblib.load("model/le_weather_conditions.pkl"),
    'Road Type': joblib.load("model/le_road_type.pkl"),
    'Road Condition': joblib.load("model/le_road_condition.pkl"),
    'Lighting Conditions': joblib.load("model/le_lighting_conditions.pkl"),
    'Driver Gender': joblib.load("model/le_driver_gender.pkl"),
    'Alcohol Involvement': joblib.load("model/le_alcohol_involvement.pkl"),
}
target_encoder = joblib.load("model/le_accident_severity.pkl")


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/map')
def map_view():
    return render_template('map.html')
@app.route('/contact')
def contact():
    return render_template("contact.html")




@app.route('/predict-form')
def predict_form():
    dropdown_options = {key: list(encoder.classes_) for key, encoder in encoders.items()}
    return render_template("index.html", options=dropdown_options)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = {
        'Day of Week': request.form['day_of_week'],
        'Vehicle Type Involved': request.form['vehicle_type'],
        'Weather Conditions': request.form['weather'],
        'Road Type': request.form['road_type'],
        'Road Condition': request.form['road_condition'],
        'Lighting Conditions': request.form['lighting'],
        'Speed Limit (km/h)': int(request.form['speed']),
        'Driver Age': int(request.form['age']),
        'Driver Gender': request.form['gender'],
        'Alcohol Involvement': request.form['alcohol']
    }

    encoded = []
    for key in input_data:
        if key in encoders:
            encoded.append(encoders[key].transform([input_data[key]])[0])
        else:
            encoded.append(input_data[key])

    pred = model.predict([encoded])[0]
    severity = target_encoder.inverse_transform([pred])[0]

    dropdown_options = {key: list(encoder.classes_) for key, encoder in encoders.items()}
    return render_template("index.html", prediction=severity, options=dropdown_options)

if __name__ == "__main__":
    app.run(debug=True)

