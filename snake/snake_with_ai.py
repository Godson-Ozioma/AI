from tkinter import *
import random

GAME_WIDTH = 1400
GAME_HEIGHT = 700
SPEED = 40
SPACE_SIZE = 30
BODY_PARTS = 1
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Agent:
    def __init__(self):
        self.minDistance = None
        self.boy_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        self.bestChoice = "down"

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)

    def updateDirection(self, x, y, currentDir, food):
        xF = food.coordinates[0]
        yF = food.coordinates[1]

        c = self.coordinates[0]
        nextRight = (x + SPACE_SIZE, y)
        nextLeft = (x - SPACE_SIZE, y)
        nextUp = (x, y - SPACE_SIZE)
        nextDown = (x, y + SPACE_SIZE)

        self.minDistance = 10000

        if currentDir != "left":
            xR, yR = nextRight
            check = any(coordinate == (xR, yR) for coordinate in self.coordinates)
            if not xR >= GAME_WIDTH and not check:
                ar = xR - xF
                if ar > 0:
                    ar *= -1

                br = yR - yF
                if br > 0: br *= -1

                rdistance = ar + br
                if rdistance < 0:
                    rdistance *= -1

                self.minDistance = min(self.minDistance, rdistance)
                if self.minDistance == rdistance:
                    self.bestChoice = "right"

        if currentDir != "right":
            xL, yL = nextLeft
            if not xL < 0:
                al = xL - xF
                if al > 0: al *= -1

                bl = yL - yF
                if bl > 0: bl *= -1

                ydistance = al + bl
                if ydistance < 0: ydistance *= -1
                self.minDistance = min(self.minDistance, ydistance)
                if self.minDistance == ydistance:
                    self.bestChoice = "left"

        if currentDir != "down":
            xU, yU = nextUp
            if not yU < 0:
                au = xU - xF
                if au > 0:
                    au *= -1

                bu = yU - yF
                if bu > 0:
                    bu *= -1

                udistance = au + bu
                if udistance < 0:
                    udistance *= -1
                self.minDistance = min(self.minDistance, udistance)
                if self.minDistance == udistance:
                    self.bestChoice = "up"

        if currentDir != "up":
            xD, yD = nextDown
            if not yD >= GAME_HEIGHT:
                a = xD - xF
                if a > 0: a *= -1

                b = yD - yF
                if b > 0: b *= -1

                distance = a + b
                if distance < 0:
                    distance *= -1
                self.minDistance = min(self.minDistance, distance)
                if self.minDistance == distance:
                    self.bestChoice = "down"

        change_direction(self.bestChoice)
        print(f"best: {self.bestChoice}")


class SmartAgentA(Agent):
    def updateDirection(self, x, y, currentDir, food):
        xF = food.coordinates[0]
        yF = food.coordinates[1]

        c = self.coordinates[0]
        nextRight = (x + SPACE_SIZE, y)
        nextLeft = (x - SPACE_SIZE, y)
        nextUp = (x, y - SPACE_SIZE)
        nextDown = (x, y + SPACE_SIZE)

        self.minDistance = 10000

        if currentDir != "left":
            xR, yR = nextRight
            check = any(coordinate == (xR, yR) for coordinate in self.coordinates)
            if not xR >= GAME_WIDTH and not check:
                ar = xR - xF
                if ar > 0:
                    ar *= -1

                br = yR - yF
                if br > 0: br *= -1

                rdistance = ar + br
                if rdistance < 0:
                    rdistance *= -1

                self.minDistance = min(self.minDistance, rdistance)
                if self.minDistance == rdistance:
                    self.bestChoice = "right"

        if currentDir != "right":
            xL, yL = nextLeft
            checkL = any(coordinate == (xL, yL) for coordinate in self.coordinates)
            if not xL < 0 and not checkL:
                al = xL - xF
                if al > 0: al *= -1

                bl = yL - yF
                if bl > 0: bl *= -1

                ydistance = al + bl
                if ydistance < 0: ydistance *= -1
                self.minDistance = min(self.minDistance, ydistance)
                if self.minDistance == ydistance:
                    self.bestChoice = "left"

        if currentDir != "down":
            xU, yU = nextUp
            checkU = any(coordinate == (xU, yU) for coordinate in self.coordinates)
            if not yU < 0 and not checkU:
                au = xU - xF
                if au > 0:
                    au *= -1

                bu = yU - yF
                if bu > 0:
                    bu *= -1

                udistance = au + bu
                if udistance < 0:
                    udistance *= -1
                self.minDistance = min(self.minDistance, udistance)
                if self.minDistance == udistance:
                    self.bestChoice = "up"

        if currentDir != "up":
            xD, yD = nextDown
            checkD = any(coordinate == (xD, yD) for coordinate in self.coordinates)
            if not yD >= GAME_HEIGHT and not checkD:
                a = xD - xF
                if a > 0: a *= -1

                b = yD - yF
                if b > 0: b *= -1

                distance = a + b
                if distance < 0:
                    distance *= -1
                self.minDistance = min(self.minDistance, distance)
                if self.minDistance == distance:
                    self.bestChoice = "down"

        change_direction(self.bestChoice)
        print(f"best: {self.bestChoice}")


class Food:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="Food")


# add a square to the beginning of the snake
def move(food):
    x, y = snake.coordinates[0]
    snake.updateDirection(x, y, direction, food)

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    return (x, y)


def eat(x, y, food):
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="AI Score: {}".format(score))
        canvas.delete("Food")
        return True
    else:
        return False


def next_turn(snake, food):
    x, y = move(food)

    if check_collisions():
        game_over()
        return

    if eat(x, y, food):
        food = Food()
    else:
        # complete movement by removing the tail of the snake
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collisions():
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print("Game over")
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print("Game over")
        return True

    # collision with body
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("Game Over")
            return True


def game_over():
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 70), text="Game Over", fill="red", tags="gameover")


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="AI Score: {}".format(score), font=('consolas', 40))
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
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# snake = Agent()
snake = SmartAgentA()
food = Food()
next_turn(snake, food)

window.mainloop()
