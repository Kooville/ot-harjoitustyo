from entities.item import Item
from database_connection import get_database_connection


def get_item_by_row(row):
    return Item(row["name"],
                row["calories"],
                row["carbs"],
                row["protein"],
                row["fat"],
                row["id"]) if row else None


class ItemRepository:
    """ Luokka, joka sisältää ruoka-aineisiin liittyvät tietokantaoperaatiot """

    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self.connection = connection

    def create_item(self, item):
        """ Lisää tietokantaan uuden ruoka-aineen

        Args:
            item: Item-olio, joka halutaan lisätä tietokantaan

        Returns:
            Item-olio, joka on lisätty tietokantaan ja jolle on asetettu id
        """

        cursor = self.connection.cursor()
        cursor.execute("insert into items (name, calories, carbs, protein, fat) "
                       "values (?, ?, ?, ?, ?)",
                       (item.name, item.calories, item.carbs, item.protein, item.fat))
        self.connection.commit()
        item.id = cursor.lastrowid
        return item

    def get_item_by_name(self, name):
        """ Hakee tietokannasta ruoka-aineen, joka vastaa annettua nimeä

        Args:
            name: Ruoka-aineen nimi, jota haetaan

        Returns:
            Item-olio, joka vastaa annettua nimeä, tai None jos ruoka-ainetta ei löydy
        """

        cursor = self.connection.cursor()
        cursor.execute("select * from items where name = ?",
                       (name,))
        row = cursor.fetchone()
        return get_item_by_row(row)

    def get_all_items(self):
        """ Hakee tietokannasta kaikki ruoka-aineet 

        Returns:
            Lista Item-olioita, jotka löytyvät tietokannasta
        """

        cursor = self.connection.cursor()
        cursor.execute("select * from items")
        rows = cursor.fetchall()
        return [get_item_by_row(row) for row in rows]

    def get_item_by_multiplier(self, item, multiplier):
        """ Palauttaa halutun ruoka-aineen ravintoarvot kerrottuna valitulla määrällä 

        Args:
            item: Item-olio, jonka ravintoarvot halutaan hakea
            multiplier: Luku, jolla halutaan kertoa ruoka-aineen ravintoarvot
        """

        multiplied_item = Item(item.name,
                               item.calories*multiplier/100,
                               item.carbs*multiplier/100,
                               item.protein*multiplier/100,
                               item.fat*multiplier/100,
                               item.id)
        return multiplied_item


item_repository = ItemRepository(get_database_connection())
