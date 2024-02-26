import psycopg2

def connect_to_db():
    dbname = 'my_project'
    user = 'postgres'
    password = '4591'
    host = 'localhost'
    port = '5432'

    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        print("Connection to database successful!")
        return conn
    except psycopg2.Error as e:
        print("Error connecting to database:", e)
        return None

def add_object_to_database(username, password):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except psycopg2.Error as e:
            print("Error adding object to database:", e)
            conn.rollback()
            cursor.close()
            conn.close()
            return False

def check_user(username, password):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            if user:
                return True
            else:
                return False
        except psycopg2.Error as e:
            print("Error checking user:", e)
            conn.close()
            return False
