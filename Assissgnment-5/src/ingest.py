# src/ingest.py
import pandas as pd
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def read_one(path: Path, date_col='timestamp', kwh_col='kwh', building=None):
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        raise
    except Exception as e:
        logger.exception(f"Failed reading {path}: {e}")
        raise

    # normalize columns
    if date_col not in df.columns:
        # try common alternatives
        for alt in ['Date','date','datetime','time','Timestamp']:
            if alt in df.columns:
                df = df.rename(columns={alt: date_col})
                break

    if kwh_col not in df.columns:
        for alt in ['kWh','energy','consumption','value']:
            if alt in df.columns:
                df = df.rename(columns={alt: kwh_col})
                break

    # add building metadata if provided or derive from filename
    if 'building' not in df.columns:
        if building:
            df['building'] = building
        else:
            df['building'] = path.stem

    # parse date
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=[date_col])
    # ensure numeric
    df[kwh_col] = pd.to_numeric(df[kwh_col], errors='coerce')
    return df[[date_col, kwh_col, 'building']]

def read_all(data_dir: str):
    data_dir = Path(data_dir)
    files = list(data_dir.glob("*.csv"))
    if not files:
        logger.warning("No CSV files found in data directory.")
    frames = []
    errors = []
    for f in files:
        try:
            bname = f.stem
            df = read_one(f, building=bname)
            frames.append(df)
            logger.info(f"Loaded {f.name} ({len(df)} rows).")
        except Exception as e:
            errors.append((f.name, str(e)))
            logger.error(f"Error loading {f.name}: {e}")
    if frames:
        combined = pd.concat(frames, ignore_index=True)
    else:
        combined = pd.DataFrame(columns=['timestamp','kwh','building'])
    return combined, errors
