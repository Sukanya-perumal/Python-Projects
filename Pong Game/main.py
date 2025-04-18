from paddle import Paddle
from ball import Ball
from scoreboard import  Scoreboard
from turtle import Screen
import  time
screen =Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")
game_on =True
speed = 10
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.y_bounce()
    if ball.distance(r_paddle) <50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.x_bounce()

    # Right paddle misses the ball
    if ball.xcor() > 380 :
        ball.reset_position()
        ball.x_bounce()
        scoreboard.l_point()
    if ball.xcor() < -380 :
        ball.reset_position()
        ball.x_bounce()
        scoreboard.r_point()


screen.exitonclick()