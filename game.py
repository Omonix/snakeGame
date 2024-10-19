import turtle
import time
import random

def lb_up():
    if head.direction != "down":
        head.direction = "up"
def lb_down():
    if head.direction != "up":
        head.direction = "down"
def lb_left():
    if head.direction != "right":
        head.direction = "left"
def lb_right():
    if head.direction != "left":
        head.direction = "right"
def lb_move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + foot)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - foot)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - foot)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + foot)

delay = 0.1
score = 0
high_score = 0
color = 0
foot = 20

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

tabColor = ['red', 'orange', 'yellow', 'green', 'turquoise', 'blue', 'violet']
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(tabColor[random.randint(0, 6)])
food.penup()
food.goto(0,100)
segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.shape("square")
pen.color("grey")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

wn.listen()
wn.onkeypress(lb_up, "z")
wn.onkeypress(lb_down, "s")
wn.onkeypress(lb_left, "q")
wn.onkeypress(lb_right, "d")

while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
    if head.distance(food) < 17:
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        food.goto(x,y)
        food.color(tabColor[random.randint(0, 6)])
        colorSnake = ['red', 'yellow', 'orange']
        if score % 4 == 0:
            if color == 2:
                color = 0
            else:
                color += 1
            foot += 0.5
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(colorSnake[color])
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    lb_move()
    for segment in segments:
        if segment.distance(head) < 17:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)