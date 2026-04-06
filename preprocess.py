import numpy as np

def add_features(df):
    df = df.copy()
    
    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
    df['day_sin'] = np.sin(2 * np.pi * df['timestamp'].dt.dayofweek / 7)
    df['day_cos'] = np.cos(2 * np.pi * df['timestamp'].dt.dayofweek / 7)

    for lag in [1, 6, 12, 24]:
        df[f'lag_{lag}'] = df['noise_level'].shift(lag)

    return df.dropna()