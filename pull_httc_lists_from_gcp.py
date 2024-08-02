from google.cloud import storage
import os
import pandas as pd
import glob
from dotenv import load_dotenv
load_dotenv('/Users/kevin/spotify/.env')

PROJECT_ID = 'kb-data-391220'

def download_files_from_bucket(bucket_name, destination_folder):
    # Initialize a client
    storage_client = storage.Client(project=PROJECT_ID)

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # Create destination folder if it does not exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List all the blobs in the bucket
    blobs = bucket.list_blobs()

    # Download each blob
    for blob in blobs:
        destination_file_name = os.path.join(destination_folder, blob.name)

        # Create directories if necessary
        if not os.path.exists(os.path.dirname(destination_file_name)):
            os.makedirs(os.path.dirname(destination_file_name))

        # Download the file
        blob.download_to_filename(destination_file_name)
        print(f'Blob {blob.name} downloaded to {destination_file_name}.')

# Example usage
bucket_name = 'kb_spotify'
destination_folder = '~/httc_playlists'
download_files_from_bucket(bucket_name, destination_folder)


# Directory containing the Parquet files
directory = '/Users/kevin/httc_playlists'

# Get a list of all Parquet files in the directory
parquet_files = glob.glob(os.path.join(directory, '*.parquet'))

# Load each Parquet file into a DataFrame and store them in a list
data_frames = [pd.read_parquet(file) for file in parquet_files]

# Concatenate all DataFrames into a single DataFrame
hat = pd.concat(data_frames, ignore_index=True)


hat.head()
hat.columns

hat.sort_values('duration_ms', inplace=False, ascending=True)[['track_name', 'length']]

def convert_ms_to_minutes_seconds(milliseconds):
    # Calculate total seconds
    total_seconds = milliseconds / 1000

    # Calculate minutes and remaining seconds
    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60

    return f'{minutes}:{seconds:.0f}'

hat['length'] = hat.duration_ms.apply(convert_ms_to_minutes_seconds)
