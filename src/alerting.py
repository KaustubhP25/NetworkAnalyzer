import logging


def setup_logging(log_file):
    # Set up logging configuration
    logging.basicConfig(filename=log_file,
                        filemode='a',
                        format='%(asctime)s - %(message)s',
                        level=logging.INFO)


def log_anomalies(df):
    # Log anomalies to the specified log file
    anomalies = df[df['anomaly'] == -1]
    if not anomalies.empty:
        logging.info("Detected anomalies:")
        for index, row in anomalies.iterrows():
            logging.info(f"Timestamp: {row['timestamp']}, Length: {row['length']}")
    else:
        logging.info("No anomalies detected in this batch")
