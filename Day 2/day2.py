f = open("input.txt", "r")

score = 0
scoredict = {'X':1, 'Y':2, 'Z':3}
# Setup dictionary for wins
windict = {'A':'Y','B':'Z','C':'X'}
# Setup dictionary for losses
losedict = {'A':'Z','B':'X','C':'Y'}
'''
A: Rock, B: Paper, C: Scissors
X: Rock, Y: Paper, Z: Scissors
'''
for line in f:
  inputs = line.split()
  opp = inputs[0]
  you = inputs[1]
  if windict[opp] == you:
    score += 6
  elif losedict[opp] == you:
    score += 0
  else:
    score += 3
  score += scoredict[you]
print(score)