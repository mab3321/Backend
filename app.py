import os
from google.cloud import storage
import pandas as pd
import random
from flask import Flask, jsonify, request
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)


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
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

    return data


# Specify the path to your CSV file and encoding
csv_file_path = read_file()  # Replace with the path to your CSV file
csv_encoding = 'utf-8'  # Replace with the appropriate encoding if needed

# Read data from the CSV file
data = read_data_from_csv(csv_file_path)




@app.route("/")
def hello_world():
    df = pd.read_csv(read_file())

    column_names = df.columns

    """Example Hello World route."""
    name = column_names
    return f"Header is : {name}!"


@app.route("/api/search", methods=["GET"])
def search_data():
    # Get the query parameter from the request URL
    query = request.args.get("query")
    limit = int(request.args.get("limit"))

    if not query:
        return jsonify([])

    # Perform a basic search on the data based on the 'query' parameter
    results = []
    for row in data:
        for key, value in row.items():
            if query.lower() in value.lower():
                results.append(row)
                break
    if len(results) > int(limit):
        return jsonify(results[:limit])
    else:
        return jsonify(results)


@app.route("/api/products", methods=["GET"])
def get_product():
    product_id = request.args.get("id")
    product_data = ''
    # Replace this with your logic to fetch product data from a database or another source
    for row in data:
        for key, value in row.items():
            if product_id in value:
                product_data = row
                break

    return jsonify(product_data)


@app.route("/api/top_products", methods=["GET"])
def top_product():
    # Replace the following line to fetch your data from a source if needed
    # product_data = data[30:46]

    # Select 16 random elements from the data list
    product_data = data[30:46]

    return jsonify(product_data)


@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
