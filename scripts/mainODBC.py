import pyodbc
import pandas as pd
from sqlalchemy import create_engine
import os
from os import listdir
from os.path import isfile, join

drivers = pyodbc.drivers()

requested_driver = 'Microsoft Access Driver (*.mdb, *.accdb)'
if not requested_driver in drivers:
    print(f"Missing requested driver {requested_driver} exit")
    exit(0)



ld = listdir("data")


access_files = [f for f in listdir("data") if os.path.isfile(join("data", f)) and os.path.splitext(f)[1] in ['.mdb', '.accdb']]

for access_file in access_files:
    conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                f'DBQ=.\\data\\{access_file};')
    conn = pyodbc.connect(conn_str)
    sqlite_file = join("./data", os.path.splitext(access_file)[0]+'.sqlite')

    if os.path.isfile(sqlite_file):
        print(f"file {sqlite_file} already exist!!! discarded")
        continue

    engine = create_engine('sqlite:///{0}'.format(join("data", os.path.splitext(access_file)[0]+'.sqlite')), echo=False)

    cursor = conn.cursor()
    for i in cursor.tables(tableType='TABLE'):
        print(i.table_name)
        df = pd.read_sql(f'select * from \"{i.table_name}\"', conn)
        df.to_sql(i.table_name, con=engine)
        print(f"table {i.table_name} of DB {access_file} imported into DB {sqlite_file}")

    print(f"file {sqlite_file} created")
