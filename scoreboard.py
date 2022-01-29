from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-30, 250)
        self.write(f"{self.l_score}", align='center' , font=('Arial', 35, 'normal'))
        self.goto(30, 250)
        self.write(f"{self.r_score}", align='center', font=('Arial', 35, 'normal'))

    def increase_score_r(self):
        self.r_score += 1
        self.update_scoreboard()

    def increase_score_l(self):
        self.l_score += 1
        self.update_scoreboard()
