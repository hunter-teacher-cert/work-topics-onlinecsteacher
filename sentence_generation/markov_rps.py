# From: How to win at rock-paper-scissors, BBC
# https://www.bbc.com/news/science-environment-27228416

# Losers, on the other hand, tended to switch to a different action.
# And they did so in order of the name of the game - moving from rock,
# to paper, to scissors.

# After losing with a rock, for example, a player was more likely to play
# paper in the next round than the "one in three" rule would predict.


import random

# Create a list for the computer's moves
computer_move = ['rock','paper','scissors']

# Create a list for player's first move
player_first_move = ['rock','paper','scissors']

# Play several rounds of rock, paper, scissors
for i in range(10):

    if i == 0:
        # Select the first move randomly from the list of strings
        computer = [random.choice(computer_move)]
        player = [random.choice(player_first_move)]

    # Determine the winner of the match up and assign it to outcome
    if computer[i] == player[i]:
        outcome = "Tie"
    elif computer[i] == 'rock' and player[i] == 'scissors':
        outcome = "Computer wins"
    elif computer[i] == 'rock' and player[i] == 'paper':
        outcome = "Player wins"
    elif computer[i] == 'paper' and player[i] == 'rock':
        outcome = "Computer wins"
    elif computer[i] == 'paper' and player[i] == 'scissors':
        outcome = "Player wins"
    elif computer[i] == 'scissors' and player[i] == 'paper':
        outcome = "Computer wins"
    elif computer[i] == 'scissors' and player[i] == 'rock':
        outcome = "Player wins"

    # Print out the number of the round
    print("Round " + str(i+1))

    # Print Computer's plays
    print('Computer: ' + str(computer[i]))

    # Print Player's plays
    print('Player: ' + str(player[i]))

    # Print the outcome of the match up
    print(outcome)

    # Update player's next move based on outcome of previous match up
    if player[i] == 'rock' and outcome != 'Computer wins':
        player_chain = {
            'rock': ['rock', 'rock', 'rock','rock','paper','scissors']
            }
        player.append(random.choice(player_chain[player[i]]))
        computer.append(random.choice(computer_move))
    elif player[i] == 'rock' and outcome == 'Computer wins':
        player_chain = {
            'rock': ['paper', 'paper', 'paper', 'paper','paper','scissors']
            }
        player.append(random.choice(player_chain[player[i]]))
        computer.append(random.choice(computer_move))
    elif player[i] == 'paper' and outcome != 'Computer wins':
        player_chain = {
            'paper': ['paper', 'paper', 'paper', 'paper','scissors','rock']
            }
        player.append(random.choice(player_chain[player[i]]))
        computer.append(random.choice(computer_move))
    elif player[i] == 'paper' and outcome == 'Computer wins':
        player_chain = {
            'paper': ['rock','rock','rock','rock','rock','scissors']
            }
        player.append(random.choice(player_chain[player[i]]))
        computer.append(random.choice(computer_move))
    elif player[i] == 'scissors' and outcome != 'Computer wins':
        player_chain = {
            'scissors': ['scissors', 'scissors', 'scissors','scissors','rock','paper']
            }
        player.append(random.choice(player_chain[player[i]]))
        computer.append(random.choice(computer_move))
    elif player[i] == 'scissors' and outcome == 'Computer wins':
        player_chain = {
            'scissors': ['rock','rock','rock','rock','rock','paper']
            }
        player.append(random.choice(player_chain[player[i]]))
        computer.append(random.choice(computer_move))

# Print computer's complete list of moves
print("Computer's moves: ")
print(computer)

# Print player's complete list of moves
print("Player's moves: " )
print(player)
