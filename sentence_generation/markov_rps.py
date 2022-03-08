# From: How to win at rock-paper-scissors, BBC

# Losers, on the other hand, tended to switch to a different action.
# And they did so in order of the name of the game - moving from rock,
# to paper, to scissors.

# After losing with a rock, for example, a player was more likely to play
# paper in the next round than the "one in three" rule would predict.



import random
outcome_chain = {
    'rock': ['rock', 'paper', 'paper', 'scissors'],
    'paper': ['paper', 'scissors','scissors','rock'],
    'scissors': ['scissors','rock', 'rock','paper']
}

outcome = [random.choice(list(outcome_chain.keys()))]

for i in range(10):
    outcome.append(random.choice(outcome_chain[outcome[i]]))

print(outcome)
