import pandas_access as mdb
from sqlalchemy import create_engine
import os
from os import listdir
from os.path import isfile, join

access_files = [f for f in listdir("./data") if isfile(join("./data", f)) and os.path.splitext(f)[1]=='.mdb']

for access_file in access_files:
    sqlite_file = join("./data", os.path.splitext(access_file)[0]+'.sqlite')

    if os.path.isfile(sqlite_file):
        print(f"file {sqlite_file} già esiste!!! scartato")
        continue

    engine = create_engine('sqlite:///{0}'.format(join("./data", os.path.splitext(access_file)[0]+'.sqlite')), echo=False)
    tlist  = [tbl for tbl in mdb.list_tables(join("./data", access_file))]
    tables = {}

    for tbl in tlist:
        try:
            table = mdb.read_table(join("./data", access_file), tbl, encoding='ascii')
            tables[tbl] = table
        except:
            print(f"tabella {tbl} di {access_file} scartata. non riesco a leggerla")
            continue

    for tab in tables:
        print(f"tabella {tab} di  {access_file} trasferita in {sqlite_file}")
        tables[tab].to_sql(tab, con=engine)

    print(f"file {sqlite_file} creato")
