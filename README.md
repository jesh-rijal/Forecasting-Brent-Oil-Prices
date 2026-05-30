# 🛢️ Forecasting Brent Oil Prices

## 📌 Project Overview

This project focuses on forecasting Brent crude oil prices using multiple time-series forecasting models, including:

* 📈 ARIMA
* 📊 SARIMA
* 🔮 Prophet
* 📉 Exponential Smoothing (ETS)

The main objective of this project is to analyze historical Brent oil price trends and build a robust forecasting system capable of handling:

* 📅 Long-term trends
* 🔄 Structural changes
* 📉 Market volatility
* 🌍 External global shocks

The final deployed forecasting model is the **🔮 Prophet model**, selected based on overall forecasting stability and cross-validation performance.

---

# 📂 Dataset Information

* **Dataset Name:** Brent Oil Prices
* **Source:** U.S. Energy Information Administration (EIA)
* **Rows:** 9,011
* **Columns:** 2

  * 📅 `Date`
  * 💲 `Price`

### ⏳ Time Period

* From: `20-May-1987`
* To: `14-Nov-2022`

---

# 🔄 Project Workflow

## 🧹 1. Data Cleaning

The following preprocessing steps were performed:

* ✅ Checked missing values
* ✅ Checked duplicate records
* ✅ Checked outliers using Z-score
* ✅ Checked missing timestamps using `pd.date_range()`
* ✅ Handled missing timestamps using forward filling
* ✅ Converted date column into datetime format
* ✅ Set date column as DataFrame index

---

## ⚙️ 2. Feature Engineering

Created time-based features such as:

* 📆 Day of week
* 📅 Day of month

Performed:

* 🔄 Resampling
* 📉 Differencing
* 📊 Rolling statistics generation

---

# 🤖 Models Developed

## 📈 ARIMA

* ARIMA(1,1,0)
* Trend component included

## 📊 SARIMA

* order=(2,1,1)
* seasonal_order=(1,1,1,7)

## 🔮 Prophet

Included:

* 🔄 Changepoint detection
* ⚙️ Seasonality tuning
* 🌍 External regressors:

  * Financial crisis
  * COVID-19
  * Russia–Ukraine war
  * Oil supply shock

## 📉 ETS (Exponential Smoothing)

Included:

* 📈 Trend handling
* 📉 Damped trend
* 🔄 Log transformation
* 📊 Variance stabilization

---

# 📏 Model Evaluation

Models were evaluated using:

* 📉 RMSE
* 📉 MAE
* 📉 MAPE

Time-based cross-validation was performed using:

```python
TimeSeriesSplit
```

---

# 🏆 Final Model Selection

The **🔮 Prophet model** was selected as the final forecasting model because it:

* ✅ Handled structural changes effectively
* ✅ Adapted better to external market shocks
* ✅ Produced more stable forecasts
* ✅ Achieved stronger cross-validation performance

---

# 🚀 Model Deployment

The project was deployed using:

* 🌐 **Streamlit** for web application deployment
* 💾 **Joblib** for model serialization

The Streamlit application includes:

* 🎛️ Forecast horizon selection
* 📈 Historical data visualization
* 🌍 Shock event controls
* 📊 Forecast plots
* ⬇️ Downloadable forecast results

---

# 📁 Project Structure

```bash
project-folder/
│
├── BrentOilPrices.csv
├── prophet_model.pkl
├── app.py
├── requirements.txt
├── README.md
├── Documentation of Brent Oil Prices.pdf
└── brent_oil_prices.ipynb
```

---


# 🚀 How to Run the Project

## 1️⃣ 🖥️ Open Git Bash

## 2️⃣ 📥 Clone Repository

```bash
git clone https://github.com/jesh-rijal/Foresting-Brent-Oil-Prices.git
```

---

## 3️⃣ 📂 Move into Project Folder

```bash
cd Foresting-Brent-Oil-Prices
```

---

## 4️⃣ 💻 Open the Project in VS Code

```bash
code .
```

---

## 5️⃣ 🛠️ Create Virtual Environment (Recommended)

### <img src="https://img.icons8.com/color/48/windows-10.png" width="20"/> Windows

In Terminal:

```bash
python -m venv venv
venv\Scripts\activate
```

### <img src="https://img.icons8.com/color/48/mac-client.png" width="20"/> Mac / <img src="https://img.icons8.com/color/48/linux--v1.png" width="20"/> Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 6️⃣ 📦 Install Required Libraries

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install pandas numpy matplotlib scikit-learn statsmodels prophet streamlit joblib
```

---

## 7️⃣ 🚀 Run the Application

In Terminal:

```bash
streamlit run app.py
```

---

## 8️⃣ 🌐 Open in Browser

```text
http://localhost:8501
```

---

# ✨ Streamlit Features

The application allows users to:

* 🎛️ Select forecast horizon
* 📈 Visualize historical Brent oil prices
* 🔮 Generate future forecasts
* 🌍 Enable/disable global shock events
* 📊 View forecast confidence intervals
* ⬇️ Download forecast results as CSV

---

# 📋 Example Forecast Output

The forecast includes:

* 💲 Predicted oil price
* 📉 Lower confidence interval
* 📈 Upper confidence interval

---

# 🔄 Cross-Validation

Time-series cross-validation was implemented using:

```python
TimeSeriesSplit(
    n_splits=5,
    test_size=180
)
```

This ensures that the model is evaluated on unseen future data while preserving chronological order.

---

# 🛠️ Technologies Used

* 🐍 Python
* 🐼 Pandas
* 🔢 NumPy
* 📊 Matplotlib
* 📈 Statsmodels
* 🔮 Prophet
* 🤖 Scikit-learn
* 🌐 Streamlit
* 💾 Joblib

---

# 🔮 Future Improvements

Possible future improvements:

* ⚙️ Hyperparameter tuning
* 🌍 Real-time oil price API integration
* 🧠 Advanced deep learning models (LSTM/GRU)
* 📊 Interactive dashboard enhancements
* 🚀 Multi-step forecasting optimization

---

# 👨‍💻 Author

```bash
Name: Jesh Rijal
Github: [My GitHub Profile](https://github.com/jesh-rijal)
```

---

# 🔓 License
This project is open-source and available for educational and learning purposes.
