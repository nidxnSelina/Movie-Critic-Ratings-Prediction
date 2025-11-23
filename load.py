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

# --- Query the movies table in the public schema ---
query = """
SELECT *
FROM public.movies
LIMIT 10;
"""

df = pd.read_sql(query, conn)

print(df.head())

# --- Close the connection ---
conn.close()
