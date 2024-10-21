import pyodbc

connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=LUFFY\SQLEXPRESS;'
    'DATABASE=cs_transport_management;'
    'Trusted_Connection=yes;'   
)

try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("Connection successful!")

    # Example query
    cursor.execute("SELECT * FROM vehicles")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

except Exception as e:
    print(f"Error: {e}")