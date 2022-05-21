
from turtle import Turtle,Screen
from pingpong import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Ping Pong ")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Scoreboard()


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor() < (-280):#HIT THE WALL
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < (-320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.left_score()
        
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_score()

screen.exitonclick()

