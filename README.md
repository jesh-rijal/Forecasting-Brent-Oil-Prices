Brent Oil Price Forecasting using Time Series Models

Project Overview
This project focuses on forecasting Brent crude oil prices using multiple time-series forecasting models, including:            
    • ARIMA      
    • SARIMA      
    • Prophet        
    • Exponential Smoothing (ETS)      

The main objective of this project is to analyze historical Brent oil price trends and build a robust forecasting system capable of handling:         
    • Long-term trends      
    • Structural changes       
    • Market volatility      
    • External global shocks       

The final deployed forecasting model is the Prophet model, selected based on overall forecasting stability and cross-validation performance.

Dataset Information      
    • Dataset Name: Brent Oil Prices         
    • Source: U.S. Energy Information Administration (EIA)        
    • Rows: 9,011         
    • Columns: 2        
        o Date        
        o Price          
Time Period     
    • From: 20-May-1987        
    • To: 14-Nov-2022         

Project Workflow
1. Data Cleaning              

The following preprocessing steps were performed:        
    • Checked missing values            
    • Checked duplicate records          
    • Checked outliers using Z-score           
    • Checked missing timestamps using pd.date_range()       
    • Handled missing timestamps using forward filling       
    • Converted date column into datetime format        
    • Set date column as DataFrame index          

2. Feature Engineering

Created time-based features such as:      
    • Day of week          
    • Day of month       

Performed:       
    • Resampling       
    • Differencing        
    • Rolling statistics generation       

Models Developed             
  ARIMA      
    • ARIMA(1,1,0)          
    • Trend component included           
    
  SARIMA          
    • order=(2,1,1)         
    • seasonal_order=(1,1,1,7)       
               
  Prophet          
  Included:         
    • Changepoint detection        
    • Seasonality tuning       
    • External regressors:         
        o Financial crisis        
        o COVID-19           
        o Russia–Ukraine war       
        o Oil supply shock        

ETS (Exponential Smoothing)          
Included:            
    • Trend handling          
    • Damped trend           
    • Log transformation           
    • Variance stabilization          
 
Model Evaluation           
Models were evaluated using:       
    • RMSE               
    • MAE         
    • MAPE         
Time-based cross-validation was performed using:            
TimeSeriesSplit            

Final Model Selection              
The Prophet model was selected as the final forecasting model because it:            

  • Handled structural changes effectively              
  • Adapted better to external market shocks            
  • Produced more stable forecasts          
  • Achieved stronger cross-validation performance            
           
Model Deployment      
The project was deployed using:          
  • Streamlit for web application deployment           
  • Joblib for model serialization           

The Streamlit application includes:          
  • Forecast horizon selection             
  • Historical data visualization             
  • Shock event controls        
  • Forecast plots           
  • Downloadable forecast results         
  • Project Structure       
     
project-folder/        
│             
├── BrentOilPrices.csv        
├── prophet_model.pkl              
├── app.py          
├── requirements.txt      
├── README.md       
├── Documentation of Brent Oil Prices.pdf          
└── brent_oil_prices.ipynb            

Installation Guide        
1. Clone Repository:           
   git clone https://github.com/your-username/brent-oil-price-forecasting.git           
2. Move into Project Folder:          
   cd brent-oil-price-forecasting     
3. Create Virtual Environment (Recommended):       
   Winddows        
   python -m venv venv        
   venv\Scripts\activate      

   Mac/Linux        
   python3 -m venv venv        
   source venv/bin/activate         
   Install Required Libraries           
   pip install -r requirements.txt           
 
Required Libraries           
Example libraries used in this project:           
   • pandas     
   • numpy      
   • matplotlib        
   • scikit-learn    
   • statsmodels          
   • prophet        
   • streamlit           
   • joblib      
   
Run Streamlit Application     
   • streamlit run app.py    
   
Streamlit Features          
The application allows users to:          
    • Select forecast horizon         
    • Visualize historical Brent oil prices         
    • Generate future forecasts         
    • Enable/disable global shock events     
    • View forecast confidence intervals       
    • Download forecast results as CSV      

Example Forecast Output        
The forecast includes:              
    • Predicted oil price             
    • Lower confidence interval           
    • Upper confidence interval           
  
Cross-Validation       
Time-series cross-validation was implemented using:        
  TimeSeriesSplit(       
      n_splits=5,           
      test_size=180           
  )            
This ensures that the model is evaluated on unseen future data while preserving chronological order.            

Technologies Used                   
    • Python               
    • Pandas                  
    • NumPy                   
    • Matplotlib                     
    • Statsmodels                     
    • Prophet                 
    • Scikit-learn                   
    • Streamlit                
    • Joblib                  
    
Future Improvements                  
Possible future improvements:                
    • Hyperparameter tuning             
    • Real-time oil price API integration             
    • Advanced deep learning models (LSTM/GRU)              
    • Interactive dashboard enhancements             
    • Multi-step forecasting optimization                    
