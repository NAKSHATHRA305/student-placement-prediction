from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)   #creates backend server
CORS(app)   #allows react frontend to send requests

# load trained model
model = joblib.load(open("../placement_model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    age = int(data["Age"])
    cgpa = float(data["CGPA"])
    internships = int(data["Internships"])
    projects = int(data["Projects"])
    backlogs = int(data["Backlogs"])

    input_data = np.array([[age, cgpa, internships, projects, backlogs]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        result = "Placed"
    else:
        result = "Not Placed"

    return jsonify({"prediction": result})


if __name__ == "__main__":
    app.run(debug=True)