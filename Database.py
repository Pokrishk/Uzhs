import sqlite3
class Database():
    conn = sqlite3.connect('Компьютерный клуб')
    cursor = conn.cursor()
    def executeQuerry(self, query, value = None):
        try:
            with self.conn:
                if value:
                    self.cursor.execute(query, value)
                else:
                    self.cursor.execute(query)
                return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")
    def InsertData(self, table, data):
        columns = ", ".join(data.keys())
        placeholders = ", ".join("?" for _ in data)
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.executeQuerry(query, tuple(data.values()))
    def updatedata(self, table, data, condition):
        update = ", ".join(f"{column} = ?" for column in data.keys())
        query = f"UPDATE {table} SET {update} WHERE {condition.keys()[0]} = ?"
        self.executeQuerry(query, tuple(data.values()+list(condition.values())[0]))
    def deletedata(self, table, condition):
        query = f"DELETE FROM {table} IF EXISTS WHERE {condition.keys()[0]} = ?"
        self.executeQuerry(query, tuple(list(condition.values())[0]))
    def getdata(self, table):
        query = f"SELECT * FROM {table}"
        self.executeQuerry(query)
    @staticmethod
    def getcondition(condition):
        if len(condition > 1):
            conditions = " AND ".join(f"{column} = ?" for column in condition.keys())
        else: conditions = condition
        return conditions
    def getid(self, table, condition):
        conditions = self.getcondition(condition)
        query = f"SELECT id FROM {table} WHERE {conditions}"
        self.executeQuerry(query, tuple(condition.values))
    def filterdata(self, table, condition):
        conditions = self.getcondition(condition)
        query = f"SELECT * FROM {table} WHERE {conditions}"
        self.executeQuerry(query, tuple(condition.values))