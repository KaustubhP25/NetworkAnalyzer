# VISUALIZE DATA
# BY: KAUSTUBH

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_csv(file_name):
    df = pd.read_csv(file_name)
    return df

def visualize_data(df):
    # Packet count over time
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')
    df.set_index('Timestamp', inplace=True)
    packet_count = df.resample('T').size()

    plt.figure(figsize=(10, 6))
    packet_count.plot()
    plt.title("Packet Count Over Time")
    plt.xlabel("Time")
    plt.ylabel("Number of Packets")
    plt.show()

    # Distribution of protocols
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Protocol', data=df)
    plt.title("Protocol Distribution")
    plt.xlabel("Protocol")
    plt.ylabel("Count")
    plt.show()

    # Traffic sources and destinations
    plt.figure(figsize=(10, 6))
    top_sources = df['Source'].value_counts().head(10)
    sns.barplot(x=top_sources.index, y=top_sources.values)
    plt.title("Top 10 Traffic Sources")
    plt.xlabel("Source IP")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 6))
    top_destinations = df['Destination'].value_counts().head(10)
    sns.barplot(x=top_destinations.index, y=top_destinations.values)
    plt.title("Top 10 Traffic Destinations")
    plt.xlabel("Destination IP")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()
