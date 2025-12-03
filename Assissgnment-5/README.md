# 📊 Assignment 5 – Campus Energy Dashboard (Python Capstone Project)

This project implements a Campus Energy Monitoring Dashboard that ingests energy consumption data from multiple buildings (A, B, C), performs daily and weekly aggregations, generates summaries, and visualizes usage trends. The project is structured using modular Python scripts and a Jupyter Notebook for analysis.

🚀 Project Features
✔ 1. Data Ingestion

Reads multiple CSV files from the /data folder

Automatically combines data

Reports unreadable or missing files

Standardizes column names (timestamp, kwh, building)

# ✔ 2. Data Aggregation

Daily totals

Weekly usage trends

Building-wise summaries (max, min, average, total)

# ✔ 3. Object-Oriented Analysis

Uses a custom BuildingManager class to compute:

Total energy consumption

Highest-usage building

Lowest-usage building

# ✔ 4. Visualizations

Generated with Matplotlib:

Daily energy usage plot

Multi-building comparison plot

Plots are saved into /outputs.

# ✔ 5. Logging

All errors and process events are logged into:

logs/energy.log

# 📁 Project Structure

Assignment_5_Energy_Dashboard/
│
├── data/                 ← raw CSV files (BuildingA, B, C)

├── outputs/              ← generated CSVs and plots

├── logs/                 ← log file (energy.log)

├── src/

│     ├── ingest.py       ← file loading

│     ├── aggregates.py   ← daily/weekly calculations

│     ├── models.py       ← BuildingManager class

│     └── viz.py          ← plotting functions

└── notebooks/

      └── Energy_Analysis.ipynb

      🧪 How to Run the Project
      
1. Add your CSV files to /data:

Required filenames:

BuildingA_2024.csv

BuildingB_2024.csv

BuildingC_2024.csv

2. Open the Jupyter Notebook
   
notebooks/Energy_Analysis.ipynb

4. Run the cells in order (1 to 12)

These cells will:

Load data

Clean and standardize

Compute metrics

Run BuildingManager

Generate & save plots

Export outputs

daily_totals.csv

weekly_aggregates.csv

building_summary.csv

energy_usage.png

building_comparison.png

# 📌 Technologies Used

Python

Pandas

Matplotlib

OOP (Custom classes)

Logging

Modular programming

# 📜 Student Details

Name: Arpit Patni
Roll No: 2501730111
Course: B.Tech CSE – AIML
Assignment: Lab Assignment 5 – Capstone Project

🔗 GitHub Repository Link

https://github.com/arpitpaatni2007-jpg/Python-assissgnments


