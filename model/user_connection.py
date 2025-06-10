import psycopg

class UserConnection():
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect(dbname="Fast_api",
                                          user="postgres",
                                          password="Gordis31.",
                                            host="localhost",
                                            port="5432")
        except psycopg.OperationalError as e:
            print("Connection error:", e)
            self.conn.close()

    def read_all(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            return rows
        
    def read_by_id(self, id):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
            row = cursor.fetchone()
            return row if row else None

    def write(self, data):
        with self.conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (username, phone) VALUES (%(username )s, %(phone)s)", data)

        self.conn.commit()
    
    def update(self, data):
        with self.conn.cursor() as cursor:
            cursor.execute("UPDATE users SET username = %(username)s, phone = %(phone)s WHERE id = %(id)s", data)
        self.conn.commit()

    def delete(self, id):
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()