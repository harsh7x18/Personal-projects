import cx_oracle
conn = cx_oracle.connect()
cursor = conn.cursor
cursor.execute()
conn.close()