from tkinter import ttk, constants
from services.diary_service import diary_service

class CreateUserView:
    """ Käyttöliittymä uuden käyttäjän luonnille """

    def __init__(self, root):
        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._password_confirmation_entry = None
        self._error_variable = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        self._frame.destroy()

    def _handle_create_user_click(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        password_confirmation = self._password_confirmation_entry.get()

        try:
            user = diary_service.create_user(username, password, password_confirmation)
        except ValueError as error:
            self._error_variable.set(str(error))

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(row=0, column=0, padx=5, pady=5)
        self._username_entry.grid(row=0, column=1, padx=5, pady=5)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(row=1, column=0, padx=5, pady=5)
        self._password_entry.grid(row=1, column=1, padx=5, pady=5)
    
    def _initialize_password_confirmation_field(self):
        password_confirmation_label = ttk.Label(master=self._frame, text="Salasana uudestaan")
        self._password_confirmation_entry = ttk.Entry(master=self._frame, show="*") 

        password_confirmation_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_confirmation_entry.grid(row=2, column=1, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_username_field()
        self._initialize_password_field()
        self._initialize_password_confirmation_field()

        create_user_button = ttk.Button(
            master=self._frame,
            text="Luo käyttäjä",
            command=self._handle_create_user_click
        )
        create_user_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
