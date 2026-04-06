import matplotlib.pyplot as plt

def plot_time_series(df):
    fig, ax = plt.subplots(figsize=(12, 5))

    for loc in df['location'].unique():
        loc_data = df[df['location'] == loc]
        ax.plot(loc_data['timestamp'], loc_data['noise_level'], label=loc)

    ax.legend()
    ax.set_title("Noise Over Time")
    return fig