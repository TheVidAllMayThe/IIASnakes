from game import *
from human import HumanSnake
from agent1 import Agent1
from student import StudentAgent
#start the game
if __name__ == "__main__":
    snake=SnakeGame(hor=60, ver=40, fps=20)
    snake.setObstacles(15) #level of obstacles
    snake.setPlayers([
        Agent1([snake.playerPos()]),
        StudentAgent([snake.playerPos()]),
    ])
    snake.start()
