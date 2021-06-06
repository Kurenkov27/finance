import csv
import json
import sqlite3

from table_template import query


def create_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()


def add_new_elem(name, date, open_, high, low, close, adj_close, volume):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("""
        INSERT INTO data VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, date, open_, high, low, close, adj_close, volume))
    conn.commit()
    conn.close()


def write_data(elems):
    for elem in elems:
        with open(f'data/{elem}.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = next(csv_reader)
            for row in csv_reader:
                add_new_elem(elem,
                             row[0],
                             float(row[1]),
                             float(row[2]),
                             float(row[3]),
                             float(row[4]),
                             float(row[5]),
                             int(row[6])
                             )


def delete_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("""
        DELETE FROM data
    """)
    conn.commit()
    conn.close()


def get_json_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("""
            SELECT * FROM data
        """)
    row = [dict((c.description[i][0], value) \
              for i, value in enumerate(row)) for row in c.fetchall()]
    conn.close()
    return row


def get_json_elems_by_name(elem):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("""
                SELECT * FROM data
                WHERE name IS (:name)
            """, {'name': elem})
    row = [dict((c.description[i][0], value) \
              for i, value in enumerate(row)) for row in c.fetchall()]
    conn.close()
    return row


