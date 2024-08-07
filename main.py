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

character = Character(color="green", head=[(150, 90)], hands=[(120, 120), (180, 120)], belly=[(150, 120), (150, 150)], legs=([(120, 180), (180, 180)]), width=SPACE_SIZE, height=SPACE_SIZE)
character2 = Character(color="blue", head=[(270, 90)], hands=[(240, 120), (300, 120)], belly=[(270, 120), (270, 150)], legs=([(240, 180), (300, 180)]), width=SPACE_SIZE, height=SPACE_SIZE)


def update():
    character.display(canvas)
    character2.display(canvas)

    window.after(60, update)


def attack():
    character.attack()


def printf():
    print("hello kl ")


def stopAttack(canvas):
    character.reset(canvas)


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
window.bind('<Left>', lambda event: character.left_hand_attack())
window.bind('<Right>', lambda event: character.right_hand_attack())
# window.bind("<KeyRelease-Left>", lambda event: stopAttack(canvas))
# window.bind("<KeyRelease-Right>", lambda event: stopAttack(canvas))
window.bind("<KeyRelease>", lambda event: stopAttack(canvas))
# window.bind('<Up>', lambda event: change_direction('up'))
# window.bind('<Down>', lambda event: change_direction('down'))


update()
window.mainloop()
