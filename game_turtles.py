import turtle as t


class write_turtle(t.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.pencolor("white")

class line_turtle(t.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.goto(x,y)
        self.pendown()
        self.pencolor("White")
        self.pensize(5)


class snake_turtle(t.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.goto(x,y)
        self.color("white")

    

class food_turtle(t.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.goto(x,y)


