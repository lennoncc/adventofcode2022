f = open("input.txt", "r")

score = 0
# X - Lose, Y - Win, Z - Draw
rigdict = {'X':0, 'Y':3, 'Z':6}
# Rock - 1, Paper - 2, Scissors - 3
scoredict = {'A':1, 'B':2, 'C':3}
# What's needed for you to win
windict = {'A':'B','B':'C','C':'A'}
# What's needed for you to lose
losedict = {'A':'C','B':'A','C':'B'}

'''
A: Rock, B: Paper, C: Scissors
X: Lose, Y: Draw, Z: Win
1 rock 2 paper 3 scissors
'''
for line in f:
  inputs = line.split()
  opp = inputs[0]
  you = inputs[1]
  if you == 'X':
    score += scoredict[losedict[opp]]
  if you == 'Y':
    score += scoredict[opp]
  if you == 'Z':
    score += scoredict[windict[opp]]
  
  score += rigdict[you]
print(score)