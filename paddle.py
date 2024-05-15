from turtle import Turtle
STARTING_POSITIONS = [(350,0),(350,20),(350,40),(350,-20),(350,-40)]
MOVE_DISTANECE = []
UP = 90
DOWN = 270
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len=1)
        self.penup()
        self.goto(position)
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
    
    
        
        
        