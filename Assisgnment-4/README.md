# Assignment 4 — Air Quality Data Visualizer


This project analyzes real-world air quality data using Python, Pandas, and Matplotlib.
The original assignment asked for weather analysis, but the Kaggle dataset downloaded contained
pollution metrics (PM2.5, PM10, NOx, AQI, etc.) instead of temperature/rainfall.
Therefore, the assignment was adapted into an Air Quality Analysis Visualizer,
while keeping the same structure and learning outcomes.

# 📂 Project Structure

Assignment_4_Weather_Visualizer/
│
├── data/

│   └── raw_weather.csv              # original Kaggle dataset (air quality)
│
├── src/

│   ├── data_loader.py   # dataset loading & cleaning functions

│   ├── analysis.py                  # functions for AQI + pollutant statistics

│   └── visualize.py                 # plotting utilities
│
├── notebooks/

│   └── Weather_Analysis.ipynb       # main analysis & visualization notebook
│
├── outputs/

│   ├── cleaned_weather.csv          # cleaned dataset

│   ├── aqi_daily_line.png           # daily AQI trend line plot

│   ├── pm25_monthly_bar.png         # monthly PM2.5 bar chart

│   └── pm25_vs_no2_scatter.png      # pollutant scatter plot
│
├── README.md                        # project documentation (this file)

└── requirements.txt                 # required Python libraries

# 📊 Dataset Information

Source: Kaggle Air Quality Dataset

Columns include:
City, Date, PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, AQI, AQI_Bucket, Benzene, Toluene, Xylene

Since this dataset does not include temperature or rainfall,
we performed analysis on:

AQI (Air Quality Index)

PM2.5

PM10

NO2

Seasonal pollutant variations

# 🛠️ Features Implemented
✔ Data Processing

Loaded real-world CSV dataset

Parsed Date column into datetime

Set Date as index

Handled missing values with median imputation

Organized data by daily, monthly, and seasonal intervals

# ✔ Statistical Analysis

Daily AQI summary

Monthly average pollutants (PM2.5, PM10, AQI)

Seasonal AQI averages

# ✔ Visualizations

All plots saved in /outputs/ folder:

Daily AQI Trend (Line Plot)

Monthly Average PM2.5 (Bar Chart)

PM2.5 vs NO2 (Scatter Plot)

These plots provide trends, correlations, and insights.

#📈 Sample Visualizations
📌 Daily AQI Trend
outputs/aqi_daily_line.png

📌 Monthly Average PM2.5
outputs/pm25_monthly_bar.png

📌 PM2.5 vs NO2 Scatter
outputs/pm25_vs_no2_scatter.png

# 🧪 How to Run the Project
✔ 1. Install Dependencies
pip install -r requirements.txt

# ✔ 2. Open the Notebook
jupyter notebook notebooks/Weather_Analysis.ipynb

# ✔ 3. Run All Cells

This will generate:

Cleaned CSV

All visualizations

Statistics

# 📘 Key Learnings

Data cleaning & preprocessing

Handling missing values

Date-time indexing & resampling

Line, bar, and scatter plot creation

Modular Python code (src folder)

Real-world dataset analysis

# 👨‍🎓 Student Details

Name: Arpit Patni

Roll No: 2501730111

Program: B.Tech CSE (AIML)

Section: A

Submitted To: Dr. Sameer Farooq
