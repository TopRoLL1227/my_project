import psycopg2

def connect_to_db():
    dbname = 'my_project'
    user = 'postgres'
    password = '4591'
    host = 'localhost'
    port = '5432'

    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        print("Підключення до бази даних успішне!")
        return conn
    except psycopg2.Error as e:
        print("Помилка при підключенні до бази даних:", e)
        return None


if __name__ == "__main__":
    connect_to_db()
