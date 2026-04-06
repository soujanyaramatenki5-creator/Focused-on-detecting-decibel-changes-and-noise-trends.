import pandas as pd
import numpy as np

def generate_noise_data():
    dates = pd.date_range(start='2024-01-01', end='2024-03-31', freq='H')
    np.random.seed(42)
    data = []

    for date in dates:
        hour = date.hour

        if 7 <= hour <= 9:
            base = 65 + np.random.normal(0, 5)
        elif 17 <= hour <= 19:
            base = 70 + np.random.normal(0, 6)
        elif 22 <= hour or hour <= 6:
            base = 45 + np.random.normal(0, 3)
        else:
            base = 55 + np.random.normal(0, 4)

        location = np.random.choice(['Urban', 'Industrial', 'Residential', 'Commercial'])
        location_factor = {'Industrial': 15, 'Urban': 10, 'Commercial': 8, 'Residential': -8}

        noise = max(30, min(120, base + location_factor[location]))

        data.append({
            'timestamp': date,
            'noise_level': noise,
            'location': location,
            'hour': hour
        })

    return pd.DataFrame(data)