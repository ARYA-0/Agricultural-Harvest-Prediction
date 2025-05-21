🌾 Agricultural Harvest Prediction Web App

This is a responsive web-based user interface for predicting crop yields and estimating profit based on environmental and agricultural inputs. It uses HTML, Bootstrap 5, and integrates with a backend (such as Flask) for prediction logic using machine learning models.

## 📌 Features

* Predicts **agricultural yield** (in hg/ha) based on user inputs.
* Estimates **profit** using cultivation area, market price, and production cost.
* Fully responsive and styled using **Bootstrap 5**.
* Beautiful background and animated transitions for a modern user experience.
* Dropdown-assisted data entry using `datalist` for easier and more accurate input.

## 🧪 Inputs

The form collects the following inputs:

* `Year`: Year of prediction
* `Average Rainfall (mm/year)`
* `Pesticides Used (tonnes)`
* `Average Temperature (°C)`
* `Area`: Country or region
* `Item`: Crop type
* `Cultivation Area (hectares)`
* `Market Price (₹/tonne)`
* `Production Cost (₹/hectare)`

## 🔮 Outputs

* **Predicted Yield** (from ML model): Shown in hg/ha
* **Estimated Profit**: Based on formula:

  ```
  Profit = (Yield * Cultivation Area / 10000) * Market Price - (Production Cost * Cultivation Area)
  ```

## 🛠 Technologies Used

* **HTML5** and **CSS3**
* **Bootstrap 5.3** (CDN)
* Backend assumed to be **Flask** or similar (for Jinja2 templating and `/predict` route)

## 📁 Project Structure

```
project/
│
├── templates/
│   └── index.html     ← This HTML file
├── static/
│   └── style.css      ← (optional: extract styles)
├── app.py             ← Backend logic with prediction and rendering
├── model.pkl          ← Trained ML model
└── README.md
```


## 🧠 Future Enhancements

* Add charts for yield trends
* Store prediction history
* Integrate weather APIs for real-time suggestions
* Allow user login and data tracking
