import pymysql

# Fungsi untuk membuat koneksi ke database
def connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="tegal_laka_laka",
        cursorclass=pymysql.cursors.DictCursor
    )

# Fungsi untuk mengambil semua data kuliner
def fetch_all_kuliners():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM kuliner")
            rows = cursor.fetchall()
            return rows
    finally:
        connection.close()

# Fungsi untuk menambah kuliner
def insert_kuliner(name, description, price):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO kuliner (name, description, price) VALUES (%s, %s, %s)",
                (name, description, price)
            )
            connection.commit()
            return 1
    finally:
        connection.close()

# Fungsi untuk mengambil data kuliner berdasarkan id
def fetch_kuliner_by_id(kuliner_id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM kuliner WHERE id = %s", (kuliner_id,))
            row = cursor.fetchone()
            return row
    finally:
        connection.close()

# Fungsi untuk memperbarui data kuliner
def update_kuliner(kuliner_id, name, description, price):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE kuliner SET name = %s, description = %s, price = %s WHERE id = %s",
                (name, description, price, kuliner_id)
            )
            connection.commit()
            return 1
    finally:
        connection.close()

# Fungsi untuk menghapus kuliner berdasarkan id
def delete_kuliner(kuliner_id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM kuliner WHERE id = %s", (kuliner_id,))
            connection.commit()
            return 1
    finally:
        connection.close()
