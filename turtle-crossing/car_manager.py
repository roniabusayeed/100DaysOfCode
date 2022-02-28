from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        random_y = random.randint(-250, 250)
        self.goto(x=300, y=random_y)


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_amount = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Adds a new car to the list with a probability of 1/6"""
        if random.randint(1, 6) == 1:
            self.all_cars.append(Car())

    def move_cars(self):
        """Move all cars to the left of the screen by car_manager.STARTING_MOVE_DISTANCE"""
        for car in self.all_cars:
            car.forward(self.move_amount)

    def level_up(self):
        """Speeds up the cars by car_manager.MOVE_INCREMENT"""
        self.move_amount += MOVE_INCREMENT
