import psycopg
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# credentials
HOST = os.getenv("HOST")
DBNAME = os.getenv("DBNAME")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
PORT = 5432

# connect to database
conn = psycopg.connect(
    host=HOST,
    dbname=DBNAME,
    user=USERNAME,
    password=PASSWORD,
    port=PORT
)
print("Connected successfully!")

# query and save the dataset
query = """
SELECT *
FROM public.movies
"""
df = pd.read_sql(query, conn)
df.to_csv("data/movie_raw.csv")

conn.close()
