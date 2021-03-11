import sqlite3
import datetime


class DataBase:

    @staticmethod
    def make_database(data: dict):
        con = sqlite3.connect('databases/database.db')
        cur = con.cursor()
        now = datetime.datetime.now()
        name = f'Words_{now.strftime("%d_%m_%Y_%H_%M")}'

        cur.execute(f'CREATE TABLE IF NOT EXISTS {name}(Word TEXT, Amount INTEGER )')
        for key in data:
            cur.execute(f'INSERT INTO {name} VALUES ("{key}", {data[key]})')
            con.commit()
