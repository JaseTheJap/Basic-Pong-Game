# Simple Pong game in Python 3
# import module for basic graphics
import turtle
import winsound
# to get all turtle 'info' needed
# help(turtle)                # to get all functions of turtle

# create window
wn = turtle.Screen()
# # game title
wn.title("Pong by Jason Hattingh")
# # background color
wn.bgcolor("pink")
# # window size
wn.setup(width=800, height=600)
# # stops window from updating, increases game speed
wn.tracer(0)

#Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
# speed of animation, not speed of turtle
paddle_a.speed(5)
paddle_a.shape("square")
# # in order to change paddle size = FYI(default size = 20px, 20px)
paddle_a.shapesize(stretch_wid=4, stretch_len=0.5)
paddle_a.color("blue")
# in order not to draw a line as the graphic moves
paddle_a.penup()
paddle_a.goto(-350, 0)

# # Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(5)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=4, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 255)
pen.write("Player A: 0          Player B: 0", align="center", font=("Arial", 12, "bold"))

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#main loop
while True:
    # update game manually
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}         Player B: {}".format(score_a, score_b), align="center", font=("arial", 12, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}         Player B: {}".format(score_a,score_b), align="center", font=("arial", 12, "bold"))

        # Paddle and ball collision
    if (345 < ball.xcor() > 335) and (ball.ycor() < paddle_b.ycor() + 45 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(345)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (-345 > ball.xcor() < -335) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-345)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)



