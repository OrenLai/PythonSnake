from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
# pass 0 to turn the animation of the drawing off
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True

while game_on:

    # update the screen after all the movement were done
    scoreboard.show_score()
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision,  if the distance of snake head and the food < 15 , see that as collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_on = False

    # detect collision with snake tail
    # slice the segments , to exclude the snake.head
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
