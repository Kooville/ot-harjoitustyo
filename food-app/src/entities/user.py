class User:
    """ Luokka, joka sisältää yksittäisen käyttäjän """

    def __init__(self, username, password, goal_calories=0, today_calories=0):
        """ Luo uuden käyttäjän """
        self.username = username
        self.password = password
        self.goal_calories = goal_calories
        self.today_calories = today_calories
