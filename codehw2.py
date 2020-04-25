# Write your code here :-)
from microbit import *
import random
import math
PlayerX = 0
PlayerY = 0
# initialize the player's position on the XY 2 dimensions matrix
TargetX = random.randint(-50, 50)
TargetY = random.randint(-50, 50)
while True:
    X = pin0.read_analog()
    Y = pin1.read_analog()
    B = pin8.read_digital()
    # refine the joystick attribute
    Distance = math.sqrt(pow(TargetX - PlayerX, 2) + pow(TargetY - PlayerY, 2))
    # using the triangle principle to culculate the distance between Player and Target
    if Distance == 0:
        display.show(Image.HAPPY)
        sleep(2000)
        # Player wins
    if X > 430 and X < 824: 
        PlayerX = PlayerX + 1
        # go right, low speed
        if Y > 420 and Y < 823: 
            PlayerY = PlayerY - 1
            # go up, low speed
        elif Y < 400 and Y > 3:
            PlayerY = PlayerY + 1
            # go up, low speed
        elif Y >= 823:
            PlayerY = PlayerY - 2
            # go down, high speed
        elif Y <= 3:
            PlayerY = PlayerY + 2
            # go up, high speed
    elif X < 410 and X > 2:
        PlayerX = PlayerX - 1
        # go left, low speed
        if Y > 420 and Y < 823: 
            PlayerY = PlayerY - 1
            # go up, low speed
        elif Y < 400 and Y > 3:
            PlayerY = PlayerY + 1
            # go up, low speed
        elif Y >= 823:
            PlayerY = PlayerY - 2
            # go down, high speed
        elif Y <= 3:
            PlayerY = PlayerY + 2
            # go up, high speed
    elif X >= 824:
        PlayerX = PlayerX + 2
        # go right, high speed
        if Y > 420 and Y < 823: 
            PlayerY = PlayerY - 1
            # go up, low speed
        elif Y < 400 and Y > 3:
            PlayerY = PlayerY + 1
            # go up, low speed
        elif Y >= 823:
            PlayerY = PlayerY - 2
            # go down, high speed
        elif Y <= 3:
            PlayerY = PlayerY + 2
            # go up, high speed
    elif X <= 2:
        PlayerX = PlayerX - 2
        # go left, high speed
        if Y > 420 and Y < 823: 
            PlayerY = PlayerY - 1
            # go up, low speed
        elif Y < 400 and Y > 3:
            PlayerY = PlayerY + 1
            # go up, low speed
        elif Y >= 823:
            PlayerY = PlayerY - 2
            # go down, high speed
        elif Y <= 3:
            PlayerY = PlayerY + 2
            # go up, high speed
    elif X >= 410 and X <=430:
        PlayerX = PlayerX
        # go left, high speed
        if Y > 420 and Y < 823: 
            PlayerY = PlayerY - 1
            # go up, low speed
        elif Y < 400 and Y > 3:
            PlayerY = PlayerY + 1
            # go up, low speed
        elif Y >= 823:
            PlayerY = PlayerY - 2
            # go down, high speed
        elif Y <= 3:
            PlayerY = PlayerY + 2
            # go up, high speed
    else:
        PlayerX = PlayerX
        PlayerY = PlayerY
        # stay in original point
    # the distance of player position and sound position
    print(PlayerX, PlayerY, TargetX, TargetY, Distance)
    # Print the Player's coordinate and the joystick's attribute to check my code
    sleep(200)
