import psycopg2

conn = psycopg2.connect(database="dvdrental", user = "postgres", password = "prakhar", host = "127.0.0.1", port = "5432")

print("Opened database successfully")
