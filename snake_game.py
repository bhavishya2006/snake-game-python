import turtle
import time
import random

# SCREEN (girly aesthetic theme)
win = turtle.Screen()
win.title("Aesthetic Snake Game")
win.bgcolor("#bde0fe")  
win.setup(width=600, height=600)
win.tracer(0)

# SCORE
score = 0
high_score = 0

# SNAKE HEAD (rounded feel using circle shape)
head = turtle.Turtle()
head.shape("circle")
head.color("#5e60ce")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# FRUITS (multiple types)
fruits = [
    {"shape": "circle", "color": "#ffafcc", "points": 10},  
    {"shape": "circle", "color": "#ffd6a5", "points": 20},  
    {"shape": "circle", "color": "#caffbf", "points": 30},  
]

food = turtle.Turtle()
food.penup()
food.shape("circle")
food.color("#ffafcc")
food.goto(0, 100)
food.points = 10

segments = []

# SCORE DISPLAY
pen = turtle.Turtle()
pen.speed(0)
pen.color("#1d3557")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 14, "bold"))

# MOVEMENT
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# CONTROLS
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

delay = 0.12

# CHANGE FRUIT FUNCTION
def change_food():
    fruit = random.choice(fruits)
    food.shape(fruit["shape"])
    food.color(fruit["color"])
    food.points = fruit["points"]

    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    food.goto(x, y)

# MAIN LOOP
while True:
    win.update()
    time.sleep(delay)

    # border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for s in segments:
            s.goto(1000, 1000)

        segments.clear()
        score = 0
        delay = 0.12

    # eat food
    if head.distance(food) < 20:
        change_food()

        new_segment = turtle.Turtle()
        new_segment.shape("circle")
        new_segment.color("#4cc9f0")  
        new_segment.penup()
        segments.append(new_segment)

        score += food.points

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center", font=("Arial", 14, "bold"))

       
        delay -= 0.002
        if delay < 0.09:
            delay = 0.09

    # move body
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # self collision
    for s in segments:
        if s.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for s in segments:
                s.goto(1000, 1000)

            segments.clear()
            score = 0
            delay = 0.12

            pen.clear()
            pen.write(f"Game Over! Score: {score}  High Score: {high_score}",
                      align="center", font=("Arial", 14, "bold"))
