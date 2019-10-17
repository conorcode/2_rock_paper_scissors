"""
Rock Paper Scissors

Guidelines:
Rock beats Scissors
Scissors beats Paper
Paper beats Rock

Player 1 picks his/her choice

Player 2 picks his/her choice

Check the conditions that apply for each pair of inputs and determine which user wins the round

Notes:
Tie is a valid result and should be taken in consideration
Check if the inputs are not valid options and provide a message.

Improvement (With Loops):
Refactor the code so the user will play against the pc and for as long as he/she likes

Note:
Check for the scenario where computer picks rock and user picks Rock.
"""
p1_score = 0
p2_score = 0

while True:
    p1_input = False
    p2_input = False

    player_1 = input('P1 Pick your choice: ').lower()
    player_2 = input('P2 Pick your choice: ').lower()

    if player_1 == 'rock' or player_1 == 'paper' or player_1 == 'scissors':
        p1_input = True

    if player_2 == 'rock' or player_2 == 'paper' or player_2 == 'scissors':
        p2_input = True

    if p1_input == False and p2_input == False:
        print('Wrong input for both players')
    elif p1_input == False and p2_input == True:
        print('Wrong input for player 1')
    elif p1_input == True and p2_input == False:
        print('Wrong input for player 2')
    else:
        if player_1 == player_2:
            print('tie')
            p1_score += 1
            p2_score += 1
        elif player_1 == 'rock':
            if player_2 == 'paper':
                print('player 2 wins')
                p2_score += 1
            else:
                print('p1 wins')
                p1_score += 1
        elif player_1 == 'paper':
            if player_2 == 'scissors':
                print('player 2 wins')
                p2_score += 1
            else:
                print('p1 wins')
                p1_score += 1
        elif player_1 == 'scissors':
            if player_2 == 'rock':
                print('player 2 wins')
                p2_score += 1
            else:
                print('p1 wins')
                p1_score += 1

    print("The score is {} - {}".format(p1_score, p2_score))
