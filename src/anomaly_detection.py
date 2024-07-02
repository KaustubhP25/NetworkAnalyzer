# ANOMALY DETECTION
# BY: KAUSTUBH

import pandas as pd
import numpy as np
from scipy.stats import zscore


def read_csv(file_name):
    df = pd.read_csv(file_name)
    return df


def detect_anomalies(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')
    df.set_index('Timestamp', inplace=True)
    packet_count = df.resample('T').size()

    # Calculate Z-scores
    z_scores = zscore(packet_count)
    anomalies = np.where(np.abs(z_scores) > 3)

    print("Anomalies detected at:")
    for anomaly in anomalies[0]:
        print(packet_count.index[anomaly], packet_count.iloc[anomaly])
