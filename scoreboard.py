from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()
    def l_point(self):
        self.l_score +=1
        self.update_score()
    def r_point(self):
        self.r_score +=1      
        self.update_score()
    def update_score (self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,True, align= "center", font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score,True, align= "center", font=("Courier", 80, "normal"))
    def game_over(self):
        super().__init__()
        self.penup()
        self.goto(0,0)
        self.color("white")
        self.hideturtle()
        self.write("Game Over!",True, align= "center", font=("Arial", 24, "normal"))
        