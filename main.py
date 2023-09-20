"""Скрипт для заполнения данными таблиц в БД Postgres."""

# psql -h localhost -p 5432 -d test -U postgres
import csv
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="0821"
)
cur = conn.cursor()


with open('postgres-homeworks/north_data/employees_data.csv', 'r', encoding='utf-8') as csvfile:
    csv_iter = csv.reader(csvfile)
    next(csv_iter)
    for row in csv_iter:
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)

with open('postgres-homeworks/north_data/customers_data.csv', 'r', encoding='utf-8') as csvfile:
    csv_iter = csv.reader(csvfile)
    next(csv_iter)
    for row in csv_iter:
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (row))

with open('postgres-homeworks/north_data/orders_data.csv', 'r', encoding='utf-8') as csvfile:
    csv_iter = csv.reader(csvfile)
    next(csv_iter)
    for row in csv_iter:
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)


conn.commit()

cur.close()
conn.close()
