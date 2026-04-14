from entities.item import Item
from database_connection import get_database_connection


def get_item_by_row(row):
    return Item(row["name"],
                row["calories"],
                row["carbs"],
                row["protein"],
                row["fat"]) if row else None


class ItemRepository:
    """ Luokka, joka sisältää ruoka-aineisiin liittyvät tietokantaoperaatiot """

    def __init__(self, connection):
        self.connection = connection

    def create_item(self, item):
        """ Lisää tietokantaan uuden ruoka-aineen """
        cursor = self.connection.cursor()
        cursor.execute("insert into items (name, calories, carbs, protein, fat) values (?, ?, ?, ?, ?)",
                       (item.name, item.calories, item.carbs, item.protein, item.fat))
        self.connection.commit()
        return item

    def get_item_by_name(self, name):
        """ Hakee tietokannasta ruoka-aineen, joka vastaa annettua nimeä """
        cursor = self.connection.cursor()
        cursor.execute("select * from items where name = ?",
                       (name,))
        row = cursor.fetchone()
        return get_item_by_row(row)


item_repository = ItemRepository(get_database_connection())
