# src/aggregates.py
import pandas as pd

def calculate_daily_totals(df, date_col='timestamp', kwh_col='kwh'):
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.set_index(date_col)
    daily = df.groupby('building')[kwh_col].resample('D').sum().reset_index()
    return daily

def calculate_weekly_aggregates(df, date_col='timestamp', kwh_col='kwh'):
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.set_index(date_col)
    weekly = df.groupby('building')[kwh_col].resample('W').sum().reset_index()
    return weekly

def building_wise_summary(df, kwh_col='kwh', date_col='timestamp'):
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    s = df.groupby('building')[kwh_col].agg(['mean','min','max','sum','std']).reset_index()
    s = s.rename(columns={'mean':'avg_kwh','min':'min_kwh','max':'max_kwh','sum':'total_kwh','std':'std_kwh'})
    return s
