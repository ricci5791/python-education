import psycopg2


class DBConn:

    def __init__(self):
        try:
            conn = psycopg2.connect(database="postgres", user="postgres",
                                    password="postgres_password", host="localhost", )
            conn.autocommit = True
            print("connected")
        except:
            raise psycopg2.InterfaceError
        self.mycursor = conn.cursor()

    def execute(self, query, limit=None):
        self.mycursor.execute(query)
        if limit is None:
            return self.mycursor.fetchall()

        return self.mycursor.fetchmany(limit)

    def columns(self, table):
        self.mycursor.execute(f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_schema = 'public'
                AND table_name   = '{table}'
            """)
        raw_columns = self.mycursor.fetchall()
        columns = [column[0].replace('_', ' ').capitalize() for column in raw_columns]

        return columns
