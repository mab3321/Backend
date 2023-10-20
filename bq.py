# from google.cloud import bigquery

# client = bigquery.Client()

# query = """
#     SELECT * FROM `disney-a2b9f.Wp_Products.products` order by id LIMIT 10
# """
# results = client.query(query)

# print([type(result) for result in results])
# for row in results:
#     id = row['id']
#     Product_Title = row['Product_Title']
#     print(f'{id:<20} | {Product_Title}')
from google.cloud import bigquery
import pandas as pd

# Create a BigQuery client
client = bigquery.Client()

# Define your SQL query
query = """
    SELECT corpus AS title, COUNT(word) AS unique_words
    FROM `bigquery-public-data.samples.shakespeare`
    GROUP BY title
    ORDER BY unique_words DESC
    LIMIT 10
"""

# Execute the query
query_job = client.query(query)

# Convert the query results to a DataFrame
df = query_job.to_dataframe()

# Convert the DataFrame to a dictionary
result_dict = df.to_dict(orient='records')

print(result_dict)
