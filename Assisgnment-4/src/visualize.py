# src/visualize.py
import matplotlib.pyplot as plt
import pandas as pd

def plot_daily_temp(df, out_path='outputs/temp_daily_line.png'):
    """Line chart for daily temperature trends."""
    plt.figure(figsize=(10,4))
    if 'TempMax' in df.columns:
        plt.plot(df.index, df['TempMax'], label='TempMax', linewidth=0.8)
    if 'TempMin' in df.columns:
        plt.plot(df.index, df['TempMin'], label='TempMin', linewidth=0.6)
    if 'TempMean' in df.columns:
        plt.plot(df.index, df['TempMean'], label='TempMean', linewidth=0.9)
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Temperature Trends')
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()

def plot_monthly_rainfall(df, out_path='outputs/monthly_rainfall_bar.png'):
    """Bar chart for monthly rainfall totals."""
    monthly = df['Rainfall'].resample('M').sum()
    plt.figure(figsize=(8,4))
    monthly.plot(kind='bar', width=0.8)
    plt.xlabel('Month')
    plt.ylabel('Total Rainfall (mm)')
    plt.title('Monthly Rainfall Totals')
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()

def plot_humidity_vs_temp(df, out_path='outputs/humidity_temp_scatter.png'):
    """Scatter plot for humidity vs temperature (TempMean)."""
    plt.figure(figsize=(6,5))
    plt.scatter(df['TempMean'], df['Humidity'], alpha=0.5, s=10)
    plt.xlabel('TempMean (°C)')
    plt.ylabel('Humidity (%)')
    plt.title('Humidity vs Temperature')
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
