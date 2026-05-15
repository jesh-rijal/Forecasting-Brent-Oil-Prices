import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Oil Price Forecasting",
    layout="wide"
)

st.title("Brent Oil Price Forecasting")

st.write(
    "Forecast future oil prices using the trained Prophet model."
)

# Load Historical Data
df = pd.read_csv("BrentOilPrices.csv")

# Rename columns
df.rename(columns={
    'Date': 'date',
    'Price': 'price'}, inplace=True)

# Convert date column
df['date'] = pd.to_datetime(df['date'], format='mixed')

# Load Saved Prophet Model
model_prophet = joblib.load(
    "prophet_model.pkl"
)

# Sidebar Inputs
st.sidebar.header("Forecast Settings")

forecast_days = st.sidebar.slider(
    "Select Forecast Horizon (Days)",
    min_value=30,
    max_value=365,
    value=365,
    step=30
)

# Historical Visualization Inputs
st.sidebar.header("Historical Data Visualization")

history_days = st.sidebar.slider(
    "Select Historical Data Range (Days)",
    min_value=30,
    max_value=len(df),
    value=len(df),
    step=30
)

# Historical Data Plot
st.subheader("Historical Oil Price Data")

historical_data = df.tail(history_days)

fig_hist, ax_hist = plt.subplots(figsize=(14, 6))

ax_hist.plot(
    historical_data['date'],
    historical_data['price'],
    linewidth=2
)

ax_hist.set_title(
    f'Historical Brent Oil Prices - Last {history_days} Days'
)

ax_hist.set_xlabel('Date')
ax_hist.set_ylabel('Price')

ax_hist.grid(True, alpha=0.3)

st.pyplot(fig_hist)

# Create Future DataFrame
future = model_prophet.make_future_dataframe(
    periods=forecast_days,
    freq='D'
)

# User Shock Inputs
st.sidebar.subheader("Shock Event Controls")

financial_crisis = st.sidebar.checkbox(
    "Financial Crisis Impact",
    value=False
)

covid = st.sidebar.checkbox(
    "COVID Impact",
    value=False
)

ukraine_war = st.sidebar.checkbox(
    "Ukraine War Impact",
    value=True
)

supply_shock = st.sidebar.checkbox(
    "Supply Shock Impact",
    value=False
)

# Add Regressors
future['financial_crisis'] = 0
future['covid'] = 0
future['ukraine_war'] = 0
future['supply_shock'] = 0

# Financial Crisis
if financial_crisis:
    future.loc[
        (
            (future['ds'] >= '2008-09-01') &
            (future['ds'] <= '2009-06-01')
        ),
        'financial_crisis'
    ] = 1

# COVID
if covid:
    future.loc[
        (
            (future['ds'] >= '2020-03-01') &
            (future['ds'] <= '2020-12-31')
        ),
        'covid'
    ] = 1

# Ukraine War
if ukraine_war:
    future.loc[
        (
            future['ds'] >= '2022-02-24'
        ),
        'ukraine_war'
    ] = 1

# Supply Shock
if supply_shock:
    future.loc[
        (
            (future['ds'] >= '2014-06-01') &
            (future['ds'] <= '2016-02-01')
        ),
        'supply_shock'
    ] = 1

# Forecast Button
if st.button("Generate Forecast"):

    # Forecast
    forecast_prophet = model_prophet.predict(
        future
    )

    # Forecast Table
    st.subheader("Forecast Results")

    forecast_display = forecast_prophet[
        ['ds', 'yhat', 'yhat_lower', 'yhat_upper']
    ].tail(forecast_days)

    forecast_display.columns = [
        'Date',
        'Predicted Price',
        'Lower Bound',
        'Upper Bound'
    ]

    st.dataframe(
        forecast_display,
        width='stretch'
    )

    # Download Forecast Results as CSV
    csv_forecast = forecast_display.to_csv(
        index=False
    ).encode('utf-8')

    st.download_button(
        label="Download Forecast Results CSV",
        data=csv_forecast,
        file_name="forecast_results.csv",
        mime="text/csv"
    )

    # Combined Historical + Forecast Plot
    st.subheader("Historical Data and Forecast")

    fig_forecast, ax_forecast = plt.subplots(
        figsize=(16, 7)
    )

    # Historical Data
    ax_forecast.plot(
        historical_data['date'],
        historical_data['price'],
        label='Historical Prices',
        linewidth=2
    )

    # Forecast Data
    forecast_future = forecast_prophet.tail(
        forecast_days
    )

    ax_forecast.plot(
        forecast_future['ds'],
        forecast_future['yhat'],
        label='Forecast',
        linewidth=2
    )

    # Confidence Interval
    ax_forecast.fill_between(
        forecast_future['ds'],
        forecast_future['yhat_lower'],
        forecast_future['yhat_upper'],
        alpha=0.2
    )

    ax_forecast.set_title(
        'Historical and Forecasted Brent Oil Prices'
    )

    ax_forecast.set_xlabel('Date')
    ax_forecast.set_ylabel('Price')

    ax_forecast.legend()

    ax_forecast.grid(True, alpha=0.3)

    st.pyplot(fig_forecast)

    # Prophet Default Forecast Plot
    st.subheader("Full Prophet Forecast Plot")

    fig1 = model_prophet.plot(
        forecast_prophet
    )

    plt.title(
        "Prophet Forecast"
    )

    st.pyplot(fig1)

    # Trend and Seasonality
    st.subheader("Trend and Seasonality")

    fig2 = model_prophet.plot_components(
        forecast_prophet
    )

    st.pyplot(fig2)
