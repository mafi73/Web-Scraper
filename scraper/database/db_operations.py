import psycopg2

DB_CONFIG = {
    "dbname": "webscraper_db",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": 5432,
}

def connect_to_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("خطا در اتصال به دیتابیس:", e)
        return None

def create_table():
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
            CREATE TABLE IF NOT EXISTS cars (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                price VARCHAR(50),
                link TEXT
            );
            """)
            conn.commit()
            print("جدول cars با موفقیت ایجاد شد.")
        except Exception as e:
            print("خطا در ایجاد جدول:", e)
        finally:
            cur.close()
            conn.close()

def insert_data(cars):
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            for car in cars:
                cur.execute("""
                INSERT INTO cars (name, price, link) 
                VALUES (%s, %s, %s);
                """, (car["name"], car["price"], car["link"]))
            conn.commit()
            print(f"{len(cars)} رکورد با موفقیت ذخیره شد.")
        except Exception as e:
            print("خطا در درج داده‌ها:", e)
        finally:
            cur.close()
            conn.close()

def fetch_data():
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM cars;")
            rows = cur.fetchall()
            return rows
        except Exception as e:
            print("خطا در بازیابی داده‌ها:", e)
            return []
        finally:
            cur.close()
            conn.close()
