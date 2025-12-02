# src/analysis.py
import numpy as np
import pandas as pd

def daily_stats(df, col='TempMean'):
    """Return daily (already daily) stats (mean, min, max, std)."""
    ser = df[col].dropna()
    return {
        'mean': float(ser.mean()),
        'min': float(ser.min()),
        'max': float(ser.max()),
        'std': float(ser.std())
    }

def monthly_aggregation(df, agg_col='Rainfall'):
    """Group by month and compute monthly sums and means."""
    monthly = df.resample('M').agg({
        agg_col: ['sum', 'mean', 'min', 'max'],
        'TempMean': ['mean', 'min', 'max']
    })
    # Flatten columns
    monthly.columns = ['_'.join(col).strip() for col in monthly.columns.values]
    return monthly

def seasonal_stats(df, col='TempMean'):
    """Compute seasonal averages (DJF, MAM, JJA, SON) using month to season mapping."""
    df2 = df.copy()
    df2['month'] = df2.index.month
    def month_to_season(m):
        if m in [12,1,2]: return 'DJF'
        if m in [3,4,5]: return 'MAM'
        if m in [6,7,8]: return 'JJA'
        return 'SON'
    df2['season'] = df2['month'].apply(month_to_season)
    return df2.groupby('season')[col].agg(['mean','min','max','std']).reset_index()
