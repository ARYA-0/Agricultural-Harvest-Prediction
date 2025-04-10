from flask import Flask,request, render_template
import numpy as np
import pickle
import sklearn
print(sklearn.__version__)
#loading models
dtr = pickle.load(open('/Users/aryapratapsinghchauhan/Desktop/VSCODE/cyp/dtr.pkl', 'rb'))
preprocessor = pickle.load(open('/Users/aryapratapsinghchauhan/Desktop/VSCODE/cyp/preprocessor.pkl', 'rb'))

#flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = request.form['Year']
        average_rain_fall_mm_per_year = request.form['average_rain_fall_mm_per_year']
        pesticides_tonnes = request.form['pesticides_tonnes']
        avg_temp = request.form['avg_temp']
        Area = request.form['Area']
        Item  = request.form['Item']

        features = np.array([[Year,average_rain_fall_mm_per_year,pesticides_tonnes,avg_temp,Area,Item]],dtype=object)
        transformed_features = preprocessor.transform(features)
        prediction = dtr.predict(transformed_features).reshape(1,-1)

        return render_template('index.html',prediction = prediction[0][0])

if __name__=="__main__":
    app.run(debug=True)

    import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Change the port to 5001 or any other available port

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")