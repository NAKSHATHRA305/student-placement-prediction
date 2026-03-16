import joblib

model = joblib.load("placement_model.pkl")

sample_student = [[21,1,3,2,7.5,2,3,8,7,75,6,2,0]]

prediction = model.predict(sample_student)

if prediction[0] == 1:
    print("Student will be Placed")
else:
    print("Student may not be Placed")