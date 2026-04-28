class User:
    """ Luokka, joka sisältää yksittäisen käyttäjän
    
    Attributes:
        username: Käyttäjätunnus
        password: Salasana
        goal_calories: Käyttäjän asettama kalorintavoite
        today_calories: Käyttäjän tämän päivän aterioiden kalorimäärä
        user_id: Käyttäjän id tietokannassa
    """

    def __init__(self, username, password, goal_calories=0, today_calories=0, user_id=None):
        """ Luokan konstruktori, joka luo uuden käyttäjän 
        
        Args:
            username: Käyttäjätunnus
            password: Salasana
            goal_calories: Käyttäjän asettama kalorintavoite
            today_calories: Käyttäjän tämän päivän aterioiden kalorimäärä
            user_id: Käyttäjän id tietokannassa, oletuksena None
        """

        self.username = username
        self.password = password
        self.goal_calories = goal_calories
        self.today_calories = today_calories
        self.id = user_id
