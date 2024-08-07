from tkinter import *

from fighter.character import Character

GAME_WIDTH = 1400
GAME_HEIGHT = 700
SPEED = 40
SPACE_SIZE = 30
BODY_PARTS = 1
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

window = Tk()
window.title("Fighter")
window.resizable(False, False)

score = 0

label = Label(window, text="Health: {}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")  # centre the window
# window.bind('<Left>', lambda event: change_direction('left'))
# window.bind('<Right>', lambda event: change_direction('right'))
# window.bind('<Up>', lambda event: change_direction('up'))
# window.bind('<Down>', lambda event: change_direction('down'))

character = Character(head=(100, 50), hands=(), belly=(), legs=(), canvas=canvas)

window.mainloop()
