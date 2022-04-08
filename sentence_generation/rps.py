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
        did_computer_win = False
    elif computer[i] == 'rock' and player[i] == 'scissors':
        did_computer_win = True
    elif computer[i] == 'rock' and player[i] == 'paper':
        did_computer_win = False
    elif computer[i] == 'paper' and player[i] == 'rock':
        did_computer_win = True
    elif computer[i] == 'paper' and player[i] == 'scissors':
        did_computer_win = False
    elif computer[i] == 'scissors' and player[i] == 'paper':
        did_computer_win = True
    elif computer[i] == 'scissors' and player[i] == 'rock':
        did_computer_win = False

    # Print out the number of the round
    print("Round " + str(i+1))

    # Print Computer's plays
    print('Computer: ' + str(computer[i]))

    # Print Player's plays
    print('Player: ' + str(player[i]))

    # Print the outcome of the match up
    print(did_computer_win)

    # Update player's next move based on outcome of previous match up
    player_chain = {
       rock: {
         win: ['paper', 'paper', 'paper', 'paper','paper','scissors'],
         lose:  ['rock', 'rock', 'rock','rock','paper','scissors']
       },
       paper: {
         win:  ['rock','rock','rock','rock','rock','scissors'],
         lose: ['paper', 'paper', 'paper', 'paper','scissors','rock']
       },
       scissor: {
         win: ['rock','rock','rock','rock','rock','paper'],
         lose: ['scissors', 'scissors', 'scissors','scissors','rock','paper']
       },
    }

    if did_computer_win:
      player.append(random.choice(player_chain[player[i]]['lose']))
      computer.append(random.choice(computer_move))
    else:
      player.append(random.choice(player_chain[player[i]]['win']))
      computer.append(random.choice(computer_move))


# Print computer's complete list of moves
print("Computer's moves: ")
print(computer)

# Print player's complete list of moves
print("Player's moves: " )
print(player)

"""

player_chain = {
   rock: {
     win: ['paper', 'paper', 'paper', 'paper','paper','scissors'],
     lose:  ['rock', 'rock', 'rock','rock','paper','scissors']
   },
   paper: {
     win:  ['rock','rock','rock','rock','rock','scissors'],
     lose: ['paper', 'paper', 'paper', 'paper','scissors','rock']
   },
   scissor: {
     win: ['rock','rock','rock','rock','rock','paper'],
     lose: ['scissors', 'scissors', 'scissors','scissors','rock','paper']
   },
}

if computer_did win
  player.append(random.choice(player_chain[player[i]]['lose']))
  computer.append(random.choice(computer_move))
else
  player.append(random.choice(player_chain[player[i]]['win']))
  computer.append(random.choice(computer_move))
"""
