import euclid3
import entity
from entity import *

testPlayer = Player("Lee","TeamA",3,(3,3))

teamA: list[Player] = []

teamA.append(testPlayer)

print("Players name is: ", teamA[0].name)

