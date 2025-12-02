# src/data_loader.py
import pandas as pd
from pathlib import Path

def load_raw(path):
    """Load raw CSV into DataFrame."""
    return pd.read_csv(path)

def clean_weather(df,
                  date_col='Date',
                  temp_max='TempMax',
                  temp_min='TempMin',
                  rainfall='Rainfall',
                  humidity='Humidity'):
    """Clean dataframe: parse dates, handle NaNs, create mean temp, drop unused cols."""
    df = df.copy()

    # parse date
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

    # keep only relevant columns if they exist
    keep = [c for c in [date_col, temp_max, temp_min, rainfall, humidity] if c in df.columns]
    df = df[keep]

    # fill/handle missing numeric values: forward fill then fill with median
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].ffill().fillna(df[numeric_cols].median())

    # create mean temperature column if both exist
    if temp_max in df.columns and temp_min in df.columns:
        df['TempMean'] = (df[temp_max] + df[temp_min]) / 2.0
    elif temp_max in df.columns:
        df['TempMean'] = df[temp_max]
    elif temp_min in df.columns:
        df['TempMean'] = df[temp_min]

    # drop rows without date
    df = df.dropna(subset=[date_col])

    # set date index for resampling convenience
    df = df.set_index(date_col).sort_index()

    return df

def save_clean(df, out_path):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path)
