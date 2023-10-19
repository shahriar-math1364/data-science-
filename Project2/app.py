import pickle
from flask import Flask, render_template, request
import xgboost
# Load your machine learning model from the pickle file
with open('classification.pickle', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

# Define the route for the main page
@app.route('/')
def index():
    # Provide the HTML template to the client
    return render_template('index.html')


data_columns=["female", "male", "occupation_accountant", "occupation_doctor", "occupation_engineer", "occupation_lawyer", "occupation_manager", "occupation_nurse", "occupation_sales representative", "occupation_salesperson", "occupation_scientist", "occupation_software engineer", "occupation_teacher", "age", "sleep duration", "quality of sleep"]
# Define the route to handle the form submission

# Define the mapping of numeric predictions to meaningful labels
stress_level_mapping = {
    0: 'Low Stress',
    1: 'Low Stress',
    2: 'Moderate Stress',
    3: 'Moderate Stress',
    4: 'High Stress',
    5: 'High Stress'
}

occupation_options = [
    "accountant", "doctor", "engineer", "lawyer",
    "manager", "nurse", "sales representative",
    "salesperson", "scientist", "software engineer", "teacher"
]
gender_options=["female", "male"]

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve input data from the form
    occupation_features = {occupation: 0 for occupation in occupation_options}
    gender_features={gender: 0 for gender in gender_options}
    # Retrieve input data from the form
    gender = request.form.get('gender')
    age = request.form.get('age')
    sleep_duration = request.form.get('sleep_duration')
    quality_of_sleep = request.form.get('quality_of_sleep')

    # Set the selected occupation feature to 1
    selected_occupation = request.form.get('occupation')
    if selected_occupation in occupation_features:
        occupation_features[selected_occupation] = 1
    selected_gender = request.form.get('gender')
    if selected_gender in gender_features:
        gender_features[selected_gender] = 1

        # Validate that the user has made selections for all dropdowns
    if not (gender and age and sleep_duration and quality_of_sleep and selected_occupation):
        return 'Error: You must select an option for all dropdown menus.'

    
    # Perform predictions using your machine learning model
    # Replace this with your actual model prediction logic
 #   prediction = model.predict([["gender_female", "gender_male", "occupation_accountant", "occupation_doctor", "occupation_engineer", "occupation_lawyer", "occupation_manager", "occupation_nurse", "occupation_sales representative", "occupation_salesperson", "occupation_scientist", "occupation_software engineer", "occupation_teacher", "age", "sleep duration", "quality of sleep"]])
    if age=="27 or younger":
        age="27"
    if age=="59 or older":
        age="59"

    if sleep_duration=="4 or less":
        sleep_duration="4"
    if sleep_duration=="9 or above":
        sleep_duration="9"


    print([
        *gender_features.values(),
        *occupation_features.values(),
        (int(age)-27) / 32,
        (int(sleep_duration)-4) / 5,
        int(quality_of_sleep) / 5
    ])
    prediction = model.predict([[
        *gender_features.values(),
        *occupation_features.values(),
        (int(age) - 27) / 32,
        (int(sleep_duration) - 4) / 5,
        int(quality_of_sleep) / 5
    ]])
    # Convert the numeric prediction to a meaningful label
    stress_level = stress_level_mapping.get(prediction[0], 'Unknown')
    print(stress_level)
    # You can then return the prediction to the client or use it as needed
    return f'Predicted Stress Level: {stress_level}'

if __name__ == '__main__':
    app.run(port=5000)
