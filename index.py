#!/usr/bin/env python


'''
Snake & Ladder Game | Assignment 3 under GCIS-123- Software Development & Problem Solving I at RIT : A Global American
University in Dubai.

Problem:

    In this homework you should implement the Snake & Ladder game in Python
    language.

        [-] Your program should declare an array or list of 100 cells. To initialize the game,
        your program should choose 5 random cells to identify Snakes locations and
        another 5 random cells to identify Ladders locations.
        [-] At each Ladder or Snake randomly chosen cell your program should generate a
        random number between 5,94 to indicate the number of steps to go forward
        incase if it was a ladder cell or the number of steps to go backward if it was snake
        cell. Your program should use a pointer to indicate your location inside the array
        of cells.
        [-] A Current location variable should be modified to forward (incremented) or
        backward (decremented) by the number of the steps inside the cell. Be careful you
        should prevent your Current from going beyond your array lower and upper
        addresses.
        [-] At each iteration of the game your program should prompt the user to enter dice
        value from 1-6 to play and modify his location inside the game.
        [-] And according to his location you will prompt him if he reaches a snake or a ladder
        and automatically your program should modify his location again (forward or
        backward) this will continue until he reaches the cell 99.
        [-] At the end the program will prompt the user with his points which is the number
        of iterations until he reaches the cell 99.

    Notes:

        [-] All cells should be initialized to 0 before choosing snakes and ladders cells.
        [-] You program should include proper functions and functions calls to organize
        your solution

Scoring Criteria:
    
    +---------------------------------------+
    | CRITERIA                      | GRADE |
    +=======================================+
    | USING FUNCTIONS               |   1   |
    |---------------------------------------|
    | COMMENTS                      |   1   |
    |---------------------------------------|
    | MAIN                          |   1   |
    |---------------------------------------|
    | LADDER & SNAKE POSITIONS      |   1   |
    |---------------------------------------|
    | CURRENT POSITION              |   1   |
    +=======================================+
    |        TOTAL                  |   5   |
    +---------------------------------------+


Copyright (C) 2021 Aaditya Rengarajan All Rights Reserved

This program is an assignment : you are free to redistribute it and/or modify it.
Contact The Developer in case of any discrepancies.
'''

# /* importing necessary modules */

#/- to generate random cells for snakes and ladders
import random

# /* function to choose random cells for snakes and ladders */

def random_chooser(cells:list,number:int):
    """
     The function to generate a random array of n numbers from a given list of numbers.

     Parameters:
        cells (list): the list of cells to pick from.
        number (int): the length of the array to be returned.
      
     Returns:
        list: an array of n numbers picked from the input "cells" parameter.
    """

    array = []

    while len(array)<number: #/- conditional statement to ensure the array is well within the limits given

        choice = random.choice(cells) #/- generating a random cell number from the array of cells provided

        if choice not in array: #/- ensuring that there are no duplicates in the list of choices

            array.append(choice) #/- adding the random choice to the array

    return array

# /* function to generate a list of obstacles given the snakes and ladder positions */

def generate_obstacles(snakes:list,ladders:list):
    """
     The function to generate a list of obstacles given the snakes and ladder positions.

     Parameters:
        snakes (list): the list of positions of snakes
        ladders (list): the list of positions of ladders
      
    Returns:
        dict: a dictionary with key "obstacles" corresponding to a list of dictionaries of each obstacle with their parameters, and key "obstacle_indices" corresponding to a list of obstacle indices only for easy access.
    """

    obstacles = []

    for i in snakes:

        #/- adding snakes to all the obstacles

        obstacles.append({
                            "location" : int(i), #/- ensuring the position of the snake is an integer so that arithmetic operations can be performed using this resource.
                            "relocate" : -(int(random.choice(list(range(5,95))))) #/- generating a random number to relocate the player by. note that, here, we choose the negative of the random location as a snake is to recede one's position.
                          })

    for i in ladders:

        #/- adding ladders to all the obstacles

        obstacles.append({
                            "location" : int(i), #/- ensuring the position of the ladder is an integer so that arithmetic operations can be performed using this resource.
                            "relocate" : (int(random.choice(list(range(5,95))))) #/- generating a random number to relocate the player by.
                          })

    obstacleindices = []

    for i in obstacles:

        #/- generating a list of indices of the obstacles to ease reference

        obstacleindices.append(i["location"])

    return {
                "obstacles" : obstacles,
                "obstacle_indices" : obstacleindices
           }


#/- generating a list of cells in a range 1 - 101 where the upper limit 101 is not included, essentialy creating a list in the range [1,101), or [1,100]

cells = list(range(1,101))


#/- using our own custom function to generate an array of positions for snakes with the length 5

snakes = random_chooser(cells,5)

'''
when we generate ladders, we need to ensure the ladder positions are not coinciding with the positions of snakes
as such coincidence is practically impossible.

note that we compare each ladder position with each snake position using a "for i in <array>" loop instead of just
checking the condition <<snakes == ladders>> because, when we compare <<snakes == ladders>>, the position of the list
elements are also checked which, in our case, is not to be checked.
'''

#/- an indefinite loop broken only when the requirement is satisfied
while True:

    ladders = random_chooser(cells,5) #/- using our own custom function to generate an array of positions for ladders with the length 5

    for i in ladders: #/- comparing each ladder position with each snake position
        if i not in snakes:
            pass
        else:
            continue #/- "continue" resets the loop and the process of calling our own custom function to generate an array of positions for ladders with the length 5 is restarted
    break #/- the loop ends if the ladders are unique positions compared to those of snakes

generated_obstacles = generate_obstacles(snakes,ladders)

obstacles,obstacleindices = generated_obstacles["obstacles"],generated_obstacles["obstacle_indices"]

#/- obstacle generation complete.
#/- code execution results : [Finished in 124ms]


# /* main part of the game */

#/- setting flags

game_complete = False #/- the game has just begun, and ends when the game_complete flag is not False
points = 0 #/- initializing a variable for the player's points, incremented every iteration

cellindex = 0 #/- the gamers position, but expressed as the cell index, i.e. the playerr's position cell would be cells[cellindex], where cells[0] is position 1 of 100 generated cells

#/- an introduction and welcome message to the player

print('''
SNAKE AND LADDER GAME
Assignment 3 under GCIS-123- Software Development & Problem Solving I at RIT : A Global American University in Dubai.

HOW TO PLAY:
    - You will be asked to roll the dice and input your result, a number between 1 and 6, every dice-roll (hereby referred to as "iteration").
    - If you encounter a snake, you will be informed of it and your position would reduce.
    - If you encounter a ladder, you will be informed of it and your position would increase.

GAME OBJECTIVE:
    - The score is incremented every iteration. Your aim is to complete the game with the least possible score.



READY PLAYER ONE.

''')

while game_complete == False:

    #/- an indefinite loop to keep iterating until the game has been completed by the player

    points+=1 #/- points are incremented every iteration

    while 1:

        #/- an indefinite loop for result validation

        try:

            #/- catching any errors if the input is invalid

            #/- reporting player statistics for a fresh iteration/chance
            print("=================================\n")
            print("ITERATION",points,"\n---------------------------------")
            print("Your Position : ",cells[cellindex])

            #/- obtaining the dice result
            '''
            NOTE : the dice roll can be automated by using

                dice = random.choice(list(range(1,7))

            which chooses a random number in a range 1 - 7 where the upper limit 7 is not included, essentialy creating a list in the range [1,7), or [1,6]
            however, this has not been implemented so as to meet the conditions of the assignment.
            '''
            dice = int(input("Enter your result from the dice expressed a natural number between 1 and 6 (including both the limits of the range) please : "))
            
            if dice not in list(range(1,7)):

                #/- ensuring the input is well within the practical limits of a cubical dice roll, in a range 1 - 7 where the upper limit 7 is not included, essentialy creating a list in the range [1,7), or [1,6]

                raise Exception("Sorry, the input is NOT well within the practical limits of a cubical dice roll, in a range 1 - 7 where the upper limit 7 is not included, essentialy creating a list in the range [1,7), or [1,6]. Please Try Again!")
            
            cellindex+=dice
            
            try:

                #/- ensuring that python can read the "cellindex" index of the "cells" array as a valid index.

                '''
                sometimes, this may raise an error in case the cell index larger than the length of the "cells" array.
                an example of such a case would be when the player is at position 97, but inputs the number 6 from the dice,
                resulting in the final position to be 97+6=103, which is out of the range of cells, causing an impossible arithmetic problem.
                '''

                cells[cellindex]

            except:

                '''
                the solution to such an impossible problem caused would be to reset the "cellindex" to the previous value, which can
                obtained by reducing the results of the dice from the "cellindex" variable and raising a valid error to inform the player
                requesting the player to try again.
                '''

                cellindex-=dice
                
                raise Exception(f"Sorry, since your position is {cells[cellindex]}, you can not move up by {dice} steps, which is out of the range of cells, causing an impossible arithmetic problem. Please Try Again!") #/- raising a valid exception to inform the player of the same

        except:

            #/- tackling any unconsidered impossible errors

            print("Not Possible, Please try again!")

        break #/- break out of the indefinite loop if the input is absolutely valid

    if cells[cellindex] in obstacleindices:

        #/- to check if the player has encountered any obstacles

        for obstacle in obstacles:

            #/- iterating through the list of obstacles to check for the obstacle encountered

            if obstacle["location"] == cells[cellindex]:

                if obstacle["relocate"]<0: #/- if the relocation is negative, the player has encountered a snake. else, the player has encountered a ladder.

                    print("Oops! You encountered a Snake!")

                    cellindex+=obstacle["relocate"] #/- relocating the player using the "cellindex" tracker variable

                    try:

                        #/- ensuring that python can read the "cellindex" index of the "cells" array as a valid index.

                        '''
                        sometimes, this may raise an error in case the cell index larger than the length of the "cells" array.
                        '''

                        cells[cellindex]

                    except:

                        '''
                        the solution to such an impossible problem caused would be to reset the "cellindex" to the previous value, which can
                        obtained by reducing the results of the obstacle relocation from the "cellindex" variable and raising a valid error to inform the player
                        requesting the player to try again.
                        '''

                        cellindex-=obstacle["relocate"]

                        print("However, you were unaffected by the snake as it is arithmatically impossible to decrement your position by",abs(obstacle["relocate"]),"steps.")
                    
                    print("Your current position is",cells[cellindex])
                else:
                    print("Congratulations! You came across a ladder!")

                    cellindex+=obstacle["relocate"] #/- relocating the player using the "cellindex" tracker variable

                    try:

                        #/- ensuring that python can read the "cellindex" index of the "cells" array as a valid index.

                        '''
                        sometimes, this may raise an error in case the cell index larger than the length of the "cells" array.
                        an example of such a case would be when the player is at position 97, but the ladder increases the player's position by, say 10,
                        resulting in the final position to be 97+6=103, which is out of the range of cells, causing an impossible arithmetic problem.
                        '''

                        cells[cellindex]

                    except:

                        '''
                        the solution to such an impossible problem caused would be to reset the "cellindex" to the previous value, which can
                        obtained by reducing the results of the obstacle relocation from the "cellindex" variable and raising a valid error to inform the player
                        requesting the player to try again.
                        '''

                        cellindex-=obstacle["relocate"]

                        print("However, you were unaffected by the ladder as it is arithmatically impossible to increment your position by",abs(obstacle["relocate"]),"steps.")

                    print("Your current position is",cells[cellindex])

    if cells[cellindex]==cells[-1]: #/- checking it the player has reached the last possible cell

        game_complete=True #/- marking the game as complete to break out of the main loop

print("Congratulations Player One! You have completed the game!") #/- informing the game as complete
print("You have scored",points,"points.") #/- reporting the number of points scored.

#/* game over */


'''
SAMPLE OUTPUT
=============


C:/Users/Vansh/Desktop>py -3 snl.py

SNAKE AND LADDER GAME
Assignment 3 under GCIS-123- Software Development & Problem Solving I at RIT : A Global American University in Dubai.

HOW TO PLAY:
    - You will be asked to roll the dice and input your result, a number between 1 and 6, every dice-roll (hereby referred to as "iteration").
    - If you encounter a snake, you will be informed of it and your position would reduce.
    - If you encounter a ladder, you will be informed of it and your position would increase.

GAME OBJECTIVE:
    - The score is incremented every iteration. Your aim is to complete the game with the least possible score.



READY PLAYER ONE.


=================================

ITERATION 1
---------------------------------
Your Position :  1
Enter your result from the dice expressed a natural number between 1 and 6 (including both the limits of the range) please : 6
=================================

ITERATION 2
---------------------------------
Your Position :  7
Enter your result from the dice expressed a natural number between 1 and 6 (including both the limits of the range) please : 6
=================================

ITERATION 3
---------------------------------
Your Position :  13
Enter your result from the dice expressed a natural number between 1 and 6 (including both the limits of the range) please : 6
Oops! You encountered a Snake!
Your current position is 88
=================================

ITERATION 4
---------------------------------
Your Position :  88
Enter your result from the dice expressed a natural number between 1 and 6 (including both the limits of the range) please : 6
=================================

ITERATION 5
---------------------------------
Your Position :  94
Enter your result from the dice expressed a natural number between 1 and 6 (including both the limits of the range) please : 6
Congratulations Player One! You have completed the game!
You have scored 5 points.

'''
#/- COMPLETION TIMESTAMP : 17:48 12/02/21 02 12 2021 -/#