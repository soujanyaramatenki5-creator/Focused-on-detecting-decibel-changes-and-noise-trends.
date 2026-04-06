from sklearn.ensemble import RandomForestRegressor

def train_model(df, features):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(df[features], df['noise_level'])
    return model


def predict_future(model, df, features, hours):
    from datetime import timedelta
    import numpy as np
    import pandas as pd

    last = df.iloc[-24:].copy()
    predictions = []

    for _ in range(hours):
        pred = model.predict(last.iloc[-1:][features])[0]
        predictions.append(pred)

        new_row = last.iloc[-1:].copy()
        new_row['noise_level'] = pred
        new_row['timestamp'] += timedelta(hours=1)
        new_row['hour'] = new_row['timestamp'].dt.hour

        new_row['hour_sin'] = np.sin(2 * np.pi * new_row['hour'] / 24)
        new_row['hour_cos'] = np.cos(2 * np.pi * new_row['hour'] / 24)

        last = pd.concat([last, new_row], ignore_index=True)

    return predictions