from pandas_gbq import to_gbq
from google.cloud import bigquery
import pandas as pd

# # Replace "data.csv" with the path to your CSV file
# csv_file = r"c:\Users\MAB\Downloads\data.csv"

# # Read the CSV file into a DataFrame
# df = pd.read_csv(csv_file)
# # Define the schema for your table
# # Define the schema for your table as a list of dictionaries

# # Define your schema
# # schema = [
# #     bigquery.SchemaField('id', 'INTEGER', mode='NULLABLE'),
# #     bigquery.SchemaField('Product_link', 'STRING', mode='NULLABLE'),
# #     bigquery.SchemaField('Product_Title', 'STRING', mode='NULLABLE'),
# #     bigquery.SchemaField('price', 'FLOAT', mode='NULLABLE'),
# #     bigquery.SchemaField('theme_download_link', 'STRING', mode='NULLABLE'),
# #     bigquery.SchemaField('Image-src', 'STRING', mode='NULLABLE'),
# #     bigquery.SchemaField('Categories', 'STRING', mode='REPEATED'),
# #     bigquery.SchemaField('Description', 'STRING', mode='NULLABLE'),
# #     bigquery.SchemaField('SalesPage', 'STRING', mode='NULLABLE'),
# #     bigquery.SchemaField('Short_Description', 'STRING', mode='NULLABLE')
# # ]

# # # Define the BigQuery client
# # # Replace 'your-project-id' with your Google Cloud project ID
# # client = bigquery.Client(project='disney-a2b9f')
# project_id = 'disney-a2b9f'
# # # Define the dataset and table IDs
# dataset_id = 'Wp_Products'  # Replace with your dataset ID
# table_id = 'Wp_Products.products'  # Replace with your table ID

# # # Create the table with the specified schema
# # table_ref = client.dataset(dataset_id).table(table_id)
# # table = bigquery.Table(table_ref, schema=schema)
# # table = client.create_table(table)  # This line actually creates the table

# # print(f"Table {table_id} created with the specified schema.")

# # df = pd.DataFrame(data)
# to_gbq(df, table_id, project_id=project_id)
# print("DONE")
# to_gbq(table_name, project_id=project_id, if_exists='replace', table_schema=schema)


# Replace with your Google Cloud project ID
project_id = "disney-a2b9f"

# Initialize a BigQuery client
client = bigquery.Client(project=project_id)

# Define the BigQuery dataset and table information
dataset_id = "Wp_Products"  # Replace with your dataset ID
table_id = "products"  # Replace with your table ID

# Replace with the path to your CSV file
csv_file_path = r"c:\Users\MAB\Downloads\data.csv"

# Load the CSV data into a Pandas DataFrame
data_frame = pd.read_csv(csv_file_path)

# Define the destination table
destination_table = f"{project_id}.{dataset_id}.{table_id}"

# Load the Pandas DataFrame into BigQuery
job_config = bigquery.LoadJobConfig(
    # Change to WRITE_APPEND or WRITE_EMPTY if needed
    write_disposition="WRITE_APPEND",
    autodetect=True,
    max_bad_records=0    # Set to False if you want to provide a specific schema
)
# print(data_frame['Image-src'])
data_frame['price'] = data_frame['price'].replace('Free', 0)
data_frame['price'] = data_frame['price'].astype(float)
job = client.load_table_from_dataframe(
    data_frame, destination_table, job_config=job_config)
job.result()  # Wait for the job to complete

print(f"Data loaded into BigQuery table {destination_table}")
