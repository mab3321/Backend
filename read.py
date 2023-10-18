import os
from google.cloud import storage
import pandas as pd
import random
from flask import Flask, jsonify, request
from flask_cors import CORS
import csv


def read_file(bucket_name="disney-a2b9f.appspot.com", blob_name="output.csv"):
    """Read a CSV blob from GCS using file-like IO"""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Open the blob for reading
    file = blob.open("r", encoding="utf-8")

    return file


def read_data_from_csv(csv_file):
    data = []

    # Use the CSV reader to read data from the file
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        data.append(row)

    return data[:40]

# Specify the path to your CSV file and encoding
csv_file_path = read_file()  # Replace with the path to your CSV file
csv_encoding = 'utf-8'  # Replace with the appropriate encoding if needed

# Read data from the CSV file
data = read_data_from_csv(csv_file_path)
print(len(data))