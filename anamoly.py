from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(df):
    df = df.copy()

    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
    df['rolling_mean'] = df['noise_level'].rolling(window=6, min_periods=1).mean()

    features = ['noise_level', 'hour_sin', 'hour_cos', 'rolling_mean']

    model = IsolationForest(contamination=0.1, random_state=42)
    df['anomaly'] = model.fit_predict(df[features].fillna(method='bfill'))

    return df