import sqlite3 as sql


class Sql3:

    def __init__(self):
        with sql.connect("sqlite.sqlite3") as connector:
            self.connector = connector


if __name__ == "__main__":
    s = Sql3()
