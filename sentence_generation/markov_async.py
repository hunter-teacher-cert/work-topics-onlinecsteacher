#rock, paper, scissors generator

import random
outcome_chain = {
    'rock': ['rock', 'paper', 'scissors'],
    'paper': ['paper', 'scissors','rock'],
    'scissors': ['scissors','rock','paper']
}

outcome = [random.choice(list(outcome_chain.keys()))]

for i in range(10):
    outcome.append(random.choice(outcome_chain[outcome[i]]))

print(outcome)
