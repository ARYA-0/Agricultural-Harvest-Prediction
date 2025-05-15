from flask import Flask, request, render_template
import numpy as np
import pickle
import sklearn

print(sklearn.__version__)
# loading models
dtr = pickle.load(open('/Users/aryapratapsinghchauhan/Desktop/VSCODE/cyp/dtr.pkl', 'rb'))
preprocessor = pickle.load(open('/Users/aryapratapsinghchauhan/Desktop/VSCODE/cyp/preprocessor.pkl', 'rb'))

# flask app
app = Flask(__name__)

# Average crop prices (USD per tonne) - these can be overridden by user input
CROP_PRICES = {
    "Cassava": 150,
    "Maize": 200,
    "Plantains and others": 300,
    "Potatoes": 250,
    "Rice, paddy": 400,
    "Sorghum": 180,
    "Soybeans": 350,
    "Sweet potatoes": 220,
    "Wheat": 230,
    "Yams": 280
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get yield prediction inputs
        Year = request.form['Year']
        average_rain_fall_mm_per_year = request.form['average_rain_fall_mm_per_year']
        pesticides_tonnes = request.form['pesticides_tonnes']
        avg_temp = request.form['avg_temp']
        Area = request.form['Area']
        Item = request.form['Item']

        # Get profit calculation inputs
        area_hectares = float(request.form.get('area_hectares', 1))  # Default to 1 hectare if not provided
        market_price = float(request.form.get('market_price', CROP_PRICES.get(Item, 200)))  # Use default price if not provided
        production_cost = float(request.form.get('production_cost', 1000))  # Default to $1000/hectare if not provided

        # Predict yield
        features = np.array([[Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]], dtype=object)
        transformed_features = preprocessor.transform(features)
        prediction = dtr.predict(transformed_features).reshape(1, -1)
        yield_hg_per_ha = prediction[0][0]  # Yield in hg/ha

        # Convert yield to tonnes/ha (1 hg = 0.1 kg, so 100 hg = 10 kg = 0.01 tonne)
        yield_tonnes_per_ha = yield_hg_per_ha * 0.0001

        # Calculate profit
        total_yield = yield_tonnes_per_ha * area_hectares
        total_revenue = total_yield * market_price
        total_cost = production_cost * area_hectares
        profit = total_revenue - total_cost

        return render_template('index.html',
                             prediction=f"{yield_hg_per_ha:,.2f}",
                             profit=f"{profit:,.2f}",
                             area_hectares=f"{area_hectares:,.2f}",
                             market_price=f"{market_price:,.2f}")

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Change the port to 5001 or any other available port