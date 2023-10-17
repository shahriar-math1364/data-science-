import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the machine learning model
model = joblib.load('car_price_prediction.pickle')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the HTML form
    odometer = request.form['odometer']
    cylinder = request.form['cylinders']
    year = request.form['year']
    manufacturer = request.form['manufacturer']
    condition = request.form['condition']
    fuel = request.form['fuel']
    title_status = request.form['title_status']
    transmission = request.form['transmission']
    drive = request.form['drive']
    vehicle_type = request.form['type']
    paint_color = request.form['paint_color']
    size=request.form['size']
    state = request.form['state']

    if '' in [odometer,cylinder,year,manufacturer,condition,fuel,title_status,transmission,drive,vehicle_type,paint_color,size,state]:
        return 'Error: You must select an option for all dropdown menus.'

    manufacturer_options = {
        'acura': 0, 'audi': 0, 'bmw': 0, 'buick': 0, 'cadillac': 0, 'chevrolet': 0, 'chrysler': 0,
        'dodge': 0, 'fiat': 0, 'ford': 0, 'gmc': 0, 'harley-davidson': 0, 'honda': 0, 'hyundai': 0,
        'infiniti': 0, 'jaguar': 0, 'jeep': 0, 'kia': 0, 'land rover': 0, 'lexus': 0, 'lincoln': 0,
        'mazda': 0, 'mercedes-benz': 0, 'mercury': 0, 'mini': 0, 'mitsubishi': 0, 'nissan': 0,
        'pontiac': 0, 'porsche': 0, 'ram': 0, 'rover': 0, 'saturn': 0, 'subaru': 0, 'toyota': 0,
        'volkswagen': 0, 'volvo': 0,
        # Add more manufacturer options here
    }

    condition_options = {
        'condition_excellent': 0, 'condition_fair': 0, 'condition_good': 0, 'condition_like new': 0,
        'condition_new': 0, 'condition_salvage': 0,
        # Add more condition options here
    }

    fuel_options = {
        'diesel': 0, 'electric': 0, 'gas': 0, 'hybrid': 0, 'other': 0,
        # Add more fuel options here
    }

    title_status_options = {
        'clean': 0, 'lien': 0, 'mps': 0, 'rebuilt': 0,
        # Add more title status options here
    }

    transmission_options = {
        'automatic': 0, 'manual': 0,
        # Add more transmission options here
    }

    drive_options = {
        '4wd': 0, 'fwd': 0, 'rwd': 0,
        # Add more drive options here
    }

    vehicle_type_options = {
        'type_suv': 0, 'type_bus': 0, 'type_convertible': 0, 'type_coupe': 0,
        'type_hatchback': 0, 'type_mini-van': 0, 'type_offroad': 0, 'type_other': 0,
        'type_pickup': 0, 'type_sedan': 0, 'type_truck': 0, 'type_van': 0, 'type_wagon': 0,
        # Add more vehicle type options here
    }

    paint_color_options = {
        'black': 0, 'blue': 0, 'brown': 0, 'custom': 0, 'green': 0, 'grey': 0, 'orange': 0,
        'purple': 0, 'red': 0, 'silver': 0, 'white': 0, 'yellow': 0,
        # Add more paint color options here
    }

    size_options = {
        'compact': 0, 'full-size': 0, 'mid-size': 0,
        # Add more size options here
    }

    state_options = {
        'ak': 0, 'al': 0, 'ar': 0, 'az': 0, 'ca': 0, 'co': 0, 'ct': 0, 'dc': 0, 'de': 0, 'fl': 0, 'ga': 0,
        'hi': 0, 'ia': 0, 'id': 0, 'il': 0, 'in': 0, 'ks': 0, 'ky': 0, 'la': 0, 'ma': 0, 'md': 0, 'me': 0,
        'mi': 0, 'mn': 0, 'mo': 0, 'ms': 0, 'mt': 0, 'nc': 0, 'nd': 0, 'ne': 0, 'nh': 0, 'nj': 0, 'nm': 0,
        'nv': 0, 'ny': 0, 'oh': 0, 'ok': 0, 'or': 0, 'pa': 0, 'ri': 0, 'sc': 0, 'sd': 0, 'tn': 0, 'tx': 0,
        'ut': 0, 'va': 0, 'vt': 0, 'wa': 0, 'wi': 0, 'wv': 0, 'wy': 0,
        # Add more state options here
    }
    manufacturer_options[manufacturer]=1
    condition_options[condition]=1
    fuel_options[fuel]=1
    title_status_options[title_status]=1
    transmission_options[transmission]=1
    drive_options[drive]=1
    vehicle_type_options[vehicle_type]=1
    paint_color_options[paint_color]=1
    size_options[size]=1
    state_options[state]=1

    odo_str=odometer.split('-')[0]
    odo_value=int(odo_str)/220000

    cyl_value=(int(cylinder)-3)/9

    if year=='2001-or-older':
        year = '2001'


    year_value=(int(year)-2001)/21

    feature_vector = [odo_value, year_value, cyl_value,
        *manufacturer_options.values(),
        *condition_options.values(),
        *fuel_options.values(),
        *title_status_options.values(),
        *transmission_options.values(),
        *drive_options.values(),
        *vehicle_type_options.values(),
        *paint_color_options.values(),
        *size_options.values(),
        *state_options.values(),
        # Repeat this for all other features
    ]

    print(feature_vector)




    # Perform regression prediction using the loaded model
    # Adjust features accordingly based on your model

    prediction = model.predict([feature_vector])

    # Pass the prediction to the HTML template
    return f'Predicted price:${int(prediction[0])}'

if __name__ == '__main__':
    app.run(debug=True)
