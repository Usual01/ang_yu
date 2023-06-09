import time
from turtle import Screen
from snakeOOP import Snake
from food import Food
from t_score import Scoreboard
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    if snake.head.xcor()> 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game = False
        scoreboard.game_over()   
    for s in snake.segments[1:]:
        if snake.head.distance(s) < 10:
            game = False
            scoreboard.game_over()


screen.exitonclick()