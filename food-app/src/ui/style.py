from tkinter import ttk


def init_styles():
    """ Alustaa käyttöliittymän tyylit """
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TFrame",
                    background="#7fddff")

    style.configure("TLabel",
                    background="#7fddff",
                    font=("Arial", 12)
                    )

    style.configure("Title.TLabel",
                    background="#7fddff",
                    foreground="#2F2F2F",
                    font=("Arial", 36, "bold")
                    )

    style.configure("TButton",
                    background="#ffffff",
                    foreground="black",
                    font=("Arial", 12),
                    padding=5
                    )

    style.configure("Card.TFrame",
                    background="#44DDFF",
                    borderwidth=1,
                    relief="solid"
                    )

    style.configure("Card.TLabel",
                    background="#44DDFF",
                    font=("Arial", 12)
                    )

    style.configure("Card.TButton",
                    background="#FFFFFF",
                    foreground="black",
                    font=("Arial", 12),
                    padding=5
                    )

    style.configure("CardError.TLabel",
                    background="#44DDFF",
                    foreground="red",
                    font=("Arial", 12)
                    )

    return style
