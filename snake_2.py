import turtle as t
import random
import game_turtles as gt
import time

#screen
screen = t.Screen()
screen.setup(height=700,width=600)
screen.bgcolor("black")
screen.tracer(0)

#draw turtle
draw_line_tt = gt.line_turtle(x=-350,y=300)
draw_line_tt.fd(1000)

# ---------------------------------------------------------------------------------------#
score_dict = {"score":[0]}
highscore  = 0

try:
    with open(r"snake_game_score.csv",mode="r") as file:
        content = file.read()
        highscore = int(content)
except FileNotFoundError:
    with open(r"snake_game_score.csv",mode="w") as file:
        file.write("0")



    



# ---------------------------------------------------------------------------------------#

#score turtles 
score = 0
score_turtle = gt.write_turtle(x=-200,y=310)
score_turtle.write(f"Score:{score}",font=("algerian",20,"normal"))

high_score_turtle = gt.write_turtle(x=0,y=310)
high_score_turtle.write(f"High Score : {highscore}",font=("algerian",20,"normal"))

warning_turtle = gt.write_turtle(x=-150,y=0)



#creating snake
snake_list=[]
for i in (0,-20,-40):
    snake = gt.snake_turtle(x=i,y=0)
    snake_list.append(snake)


    

# --------------------------------MOVEMENT OF SNAKE--------------------------------------#

#defining movement of snake
def move_snake():
    for i in range(len(snake_list)-1,0,-1):
        new_x=snake_list[i-1].xcor()
        new_y=snake_list[i-1].ycor()
        snake_list[i].goto(new_x,new_y)
    snake_list[0].fd(10)

# ----------------------------------CONTROL SNAKE-----------------------------------------#
#def fns for controlling snake
def turn_left():
    if snake_list[0].heading()!=0:
        snake_list[0].setheading(180)

def turn_right():
    if snake_list[0].heading()!=180:
        snake_list[0].setheading(0)

def turn_up():
    if snake_list[0].heading()!=270:
        snake_list[0].setheading(90)

def turn_down():
    if snake_list[0].heading()!=90:
        snake_list[0].setheading(270)

#setting keys
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")
screen.onkey(turn_up,"Up")
screen.onkey(turn_down,"Down")
screen.listen()
# ---------------------------------FOOD EATING FUNCTION----------------------------------------#

#creating food
food = gt.food_turtle(y=random.randint(-330,280),x=random.randint(-280,280))
print(f"food location{food.xcor(),food.ycor()}")

#defining fn to eat food
def eat_food():
    if snake_list[0].distance(food)<20:
        food.goto(y=random.randint(-330,280),x=random.randint(-280,280))
        print(f"NEW_food location{food.xcor(),food.ycor()}")
        return True

# ---------------------------------COLLISION WITH WALL-----------------------------------------#

def collision_with_wall():
    x_corr = snake_list[0].xcor()
    y_corr = snake_list[0].ycor()

    if (x_corr>=290 or x_corr<=-290) or (y_corr>=290 or y_corr<=-335):
        print(snake_list[0].xcor(),snake_list[0].ycor())
        warning_turtle.write("GAME OVER!",font=("algerian",40,"normal"))
        return True

# ---------------------------------COLLISION WITH OWN---------------------------------------------- #
def collision_with_own():
    if len(snake_list)<4:
        return False
    for segement in snake_list[2:]:
        if snake_list[0].distance(segement)<10:
            warning_turtle.write("GAME OVER!",font=("algerian",40,"normal"))
            return True
    return False

# ------------------------------------UPDATING SCORE------------------------------------------------#

def score_update():
    score_turtle.undo()
    score_turtle.goto(x=-200,y=310)
    score_turtle.write(f"Score:{score}",font=("algerian",20,"normal"))

# ------------------------------INCREASING SNAKE'S LENGTH-----------------------------------------#



def add_segment():
    last_segment = snake_list[-1]
    new_segment = gt.snake_turtle(x=last_segment.xcor(),y=last_segment.ycor())
    new_segment.setheading(last_segment.heading())
    snake_list.append(new_segment)

#---------------------------------------------------------------------------------------------#


while True:
    move_snake()

    if collision_with_wall():
        break

    if collision_with_own():
        break

    if eat_food():
        score+=1
        add_segment()
        score_update()



    time.sleep(0.1)
    screen.update()
if score>highscore:
    with open(r"snake_game_score.csv",mode="w") as file:
        file.write(str(score))

score_dict["score"].append(score)
print(score_dict)
screen.mainloop()