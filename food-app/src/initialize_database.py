from database_connection import get_database_connection


def drop_tables(connection):
    """ Poistaa tietokannasta aiemmin luodut taulut """
    cursor = connection.cursor()

    cursor.execute('''
                   drop table if exists users;
                   ''')

    connection.commit()


def create_tables(connection):
    """ Luo tietokantaan uudet taulut jotka määritelty schema.sql tiedostossa """
    cursor = connection.cursor()

    with open("src/schema.sql", encoding="utf-8") as f:
        sql = f.read()
    cursor.execute(sql)

    connection.commit()


def initialize_database():
    """ Alustaa tietokannan """
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
