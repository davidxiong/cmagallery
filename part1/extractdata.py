# this script has been tested on Windows 10 with Python 3.8.0
# The tables in the cma-artworks.db are:
#  'artwork', 'artwork__creator', 'artwork__department', 'creator', 'department'
# column names for artwork:
#    id
#    accession_number
#    title
#    tombstone
# column names for artwork__creator:
#    artwork_id
#    creator_id
# column names for artwork__department:
#    artwork_id
#    department_id
# column names for creator:
#    id
#    role
#    description
# column names for department:
#    id
#    name
# The above info can be gathered by running the python script of finddbtableandcolumnnames.py
#
# JSON object structure:
# { 'artwork': {
#     'id': xx,
#     'accession_number': xx,
#     'title': xx,
#     'tombstone': xx
#     },
#   'creator': {
#     'id': xx,
#     'role': xx,
#     'description': xx
#     },
#   'department': {
#     'id': xx,
#     'name': xx
#     }
# }
# note: 'creator' is possibly empty

import sqlite3
from sqlite3 import Error
import json


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn
 
 
def create_artwork_json_objects(conn, json_obj_array):

    cur = conn.cursor()
    cur.execute("SELECT * FROM artwork;")
 
    rows = cur.fetchall()
 
    for row in rows:
        aw = {}
        aw["id"] = row[0]
        aw["accession_number"] = row[1]
        aw["title"] = row[2]
        aw["tombstone"] = row[3]
        data = {}
        data["artwork"] = aw
        json_obj_array.append(data)
 
 
def add_creator_info(conn, json_obj):

    cur = conn.cursor()
    awid = json_obj["artwork"]["id"]
    cur.execute("SELECT * FROM artwork__creator WHERE artwork_id=?;", (awid,))
    row = cur.fetchone()
    if row == None:
        json_obj["creator"] = {}
        return
    cid = row[1]
    cur.execute("SELECT * FROM creator WHERE id=?;", (cid,))
    row = cur.fetchone()
    data = {}
    data["id"] = row[0]
    data["role"] = row[1]
    data["description"] = row[2]
    json_obj["creator"] = data
 
 
def add_department_info(conn, json_obj):

    cur = conn.cursor()
    awid = json_obj["artwork"]["id"]
    cur.execute("SELECT * FROM artwork__department WHERE artwork_id=?;", (awid,))
    row = cur.fetchone()
    if row == None:
        json_obj["department"] = {}
        return
    did = row[1]
    cur.execute("SELECT * FROM department WHERE id=?;", (did,))
    row = cur.fetchone()
    data = {}
    data["id"] = row[0]
    data["name"] = row[1]
    json_obj["department"] = data


def write_output_file(output_file, output):

    with open(output_file, 'w') as outfile:
        json.dump(output, outfile)
    

def main():
    database = 'cma-artworks.db'
    output_file = 'artworks.txt'
    output = []

    conn = create_connection(database)
    with conn:
        create_artwork_json_objects(conn, output)
 
        for jobj in output:
            add_creator_info(conn, jobj)
            
            add_department_info(conn, jobj)

    write_output_file(output_file, output)
        
 
if __name__ == '__main__':
    main()

