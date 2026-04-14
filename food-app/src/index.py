from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Food diary")
    window_width = 1200
    window_height = 800
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    window.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    ui_view = UI(window)
    ui_view.start()
    window.mainloop()


if __name__ == "__main__":
    main()
