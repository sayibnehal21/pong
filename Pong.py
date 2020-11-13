# Simple Ping-Pong game in Python 3
import turtle
import winsound

win = turtle.Screen()
win.title("Ping-Pong by Mohammad Nehal Sayib")
win.bgcolor("teal")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Pong Bat A
bat_a = turtle.Turtle()
bat_a.speed(0)
bat_a.shape("square")
bat_a.color("red")
bat_a.shapesize(stretch_wid=5, stretch_len=1)
bat_a.penup()
bat_a.goto(-350, 0)

# Pong Bat B
bat_b = turtle.Turtle()
bat_b.speed(0)
bat_b.shape("square")
bat_b.color("black")
bat_b.shapesize(stretch_wid=5, stretch_len=1)
bat_b.penup()
bat_b.goto(350, 0)

# Pong Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))


# Function
def bat_a_up():
    y = bat_a.ycor()
    y += 20
    bat_a.sety(y)


def bat_a_down():
    y = bat_a.ycor()
    y -= 20
    bat_a.sety(y)


def bat_b_up():
    y = bat_b.ycor()
    y += 20
    bat_b.sety(y)


def bat_b_down():
    y = bat_b.ycor()
    y -= 20
    bat_b.sety(y)


# Keyboard Binding
win.listen()
win.onkeypress(bat_a_up, "w")
win.onkeypress(bat_a_up, "a")
win.onkeypress(bat_a_down, "d")
win.onkeypress(bat_a_down, "s")

win.onkeypress(bat_b_up, "Up")
win.onkeypress(bat_b_up, "Left")
win.onkeypress(bat_b_down, "Down")
win.onkeypress(bat_b_down, "Right")

# Main game loop
while True:
    win.update()

    # Ball Movements
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # Bat and Ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bat_b.ycor() + 40 and ball.ycor() > bat_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bat_a.ycor() + 40 and ball.ycor() > bat_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Stop Game
    if (score_a == 5 or score_b == 5):
        win.bye()
