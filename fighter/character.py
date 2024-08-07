# from fighter.app import *
import time
import asyncio


class Character:
    def __init__(self, color, head, hands, belly, legs, width, height):
        self.bodyParts = [head, hands, belly, legs]
        self.gui = []
        self.inserted = []
        self.color = "green"
        self.width = width
        self.height = height
        self.attack_range = 1
        self.color = color

    def display(self, canvas):
        self.drawHead(canvas)
        self.drawHands(canvas)
        self.drawBelly(canvas)
        self.drawLegs(canvas)

    # def drawBody(self, canvas):
    #     self.drawHead(canvas)

    def drawHead(self, canvas):
        head = self.bodyParts[0]
        for (x, y) in head:
            self.gui.insert(0,
                            canvas.create_rectangle(x, y, x + self.width, y + self.height, fill=self.color,
                                                    tags=[f"body{x}{y}", "head"]))

    def drawHands(self, canvas):
        hands = self.bodyParts[1]
        for (x, y) in hands:
            self.gui.insert(0,
                            canvas.create_rectangle(x, y, x + self.width, y + self.height, fill=self.color,
                                                    tags=[f"body{x}{y}", "hand"]))

    def drawBelly(self, canvas):
        belly = self.bodyParts[2]
        for (x, y) in belly:
            self.gui.insert(0,
                            canvas.create_rectangle(x, y, x + self.width, y + self.height, fill=self.color,
                                                    tags=[f"body{x}{y}", "belly"]))

    def drawLegs(self, canvas):
        legs = self.bodyParts[3]
        for (x, y) in legs:
            self.gui.insert(0,
                            canvas.create_rectangle(x, y, x + self.width, y + self.height, fill=self.color,
                                                    tags=[f"body{x}{y}", "legs"]))


    def attack(self):
        (x, y) = self.bodyParts[0][0]

        self.bodyParts[0].insert(0, (x - (self.width * self.attack_range), y))
        self.inserted.insert(0, (x - (self.width * self.attack_range), y))

    def right_hand_attack(self):
        hands = self.bodyParts[1]
        (x, y) = hands[1]
        hands.append((x + (self.width * self.attack_range), y))
        self.inserted.append((x + (self.width * self.attack_range), y))
        # print(self.bodyParts[0])

    def left_hand_attack(self):
        hands = self.bodyParts[1]
        (x, y) = hands[0]
        hands.append((x - (self.width * self.attack_range), y))
        self.inserted.append((x - (self.width * self.attack_range), y))

    def reset(self, canvas):
        # self.bodyParts = self.initialState.copy()
        for i in range(len(self.bodyParts)):
            for point in self.bodyParts[i]:
                if point in self.inserted:
                    x, y = point
                    canvas.delete(f"body{x}{y}")
                    self.bodyParts[i].remove(point)
        self.inserted = []
