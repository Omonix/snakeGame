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
        head.sety(y + speed)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - speed)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - speed)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + speed)

delay = 0.1
score = 0
high_score = 0
color = 0
speed = 20

wn = turtle.Screen()
wn.title("Snake game")
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

tabColor = ['#970909', '#ff7f00', '#A8A819', '#0D860D', '#01D758', '#08AAAA', '#000092', '#690D69']
color = tabColor[random.randint(0, 6)]
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(color)
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
        speed = 20
        delay = 0.1
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
    if head.distance(food) < 17:
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        food.goto(x,y)
        if score % 4 == 0:
            speed += 0.5
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(color)
        new_segment.penup()
        color = tabColor[random.randint(0, 6)]
        food.color(color)
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
            speed = 20
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)