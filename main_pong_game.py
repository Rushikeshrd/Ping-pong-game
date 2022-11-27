from asyncore import write
from turtle import Turtle, Screen
from paddle_class import Paddle
from ball_class import Ball
from scoreboard_class import Scoreboard
import time
import turtle
m=0
n=0
screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:        
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # #Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        m=scoreboard.l_point()
        if m==5:
            break
            

    #Detect when L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        n=scoreboard.r_point()
        if n==5:
            break



if m==5:
    turtle.color('white')
    style = ('Courier', 30, 'bold')
    turtle.write('Player 1 won!!', font=style, align='center')
    turtle.hideturtle()
    turtle.done()
    turtle.exitonclick()
if n==5:
    turtle.color('white')
    style = ('Courier', 30, 'bold')
    turtle.write('Player 2 won!!', font=style, align='center')
    turtle.hideturtle()
    turtle.done()
    turtle.exitonclick()    

