import sqlite3
import os.path
from typing import Union

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Sqlite3:
    """Класс для работы с БД SQlite3"""

    def __init__(self):
        db_path = os.path.join(BASE_DIR, "sqlite.db")
        self.connector = sqlite3.connect(db_path)

    def get_all_groups(self):
        """Получить все группы из БД"""
        cursor = self.connector.cursor()
        cursor.execute("SELECT * FROM groups")
        data = cursor.fetchall()
        cursor.close()
        return data

    def add_groups(self, groups: Union[list, tuple]):
        """Добавить группы в БД"""
        cursor = self.connector.cursor()

        for group in groups:
            try:
                cursor.execute("INSERT INTO [groups] (id, link, title) VALUES(?, ?, ?)", group)
            except sqlite3.IntegrityError as error:
                print(f"Возможно данная группа уже есть в базе: {group[2]}\n{error}")

        self.connector.commit()
        cursor.close()


"""
prototype

cursor = self.connector.cursor()
cursor.execute("")
cursor.close()
"""
