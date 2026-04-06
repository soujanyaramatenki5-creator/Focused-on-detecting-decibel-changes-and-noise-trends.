from sklearn.cluster import KMeans

def cluster_patterns(df):
    hourly_avg = df.groupby('hour')['noise_level'].mean().reset_index()

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    hourly_avg['cluster'] = kmeans.fit_predict(hourly_avg[['noise_level']])

    return hourly_avg