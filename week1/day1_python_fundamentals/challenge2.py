# Challenge 2 – Thor's Journey to the Light (Codingame)
# Source: https://www.codingame.com/ide/puzzle/power-of-thor-episode-1
# Goal: Move Thor to the light using directional logic


import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    move = ""

    # for vertical move
    if light_y < initial_ty :
        move += "N"
        initial_ty -= 1
    elif light_y > initial_ty :
        move += "S"
        initial_ty += 1

    #for horizontal move
    if light_x < initial_tx :
        move += "W"
        initial_tx -= 1
    elif light_x > initial_tx :
        move += "E"
        initial_tx += 1
        
 
    

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(move)
