f = open("tempinput.txt", "r")
sum = 0
wholelist = []
for line in f:
  wholelist.append(line[:-1])
# print(wholelist)
i = 0
freqdict = {}
while i < len(wholelist):
  print('First 3:')
  for j in range(i,i+3):
    # print(wholelist[j])
    for indchar in wholelist[j]:
      if indchar in freqdict:
        freqdict[indchar] += 1
      else:
        freqdict[indchar] = 1
  print(freqdict)
  print('Second 3:')
  itstime = False
  for k in range(i+3,i+6):
    # print(wholelist[k])
    if itstime:
      break
    for indchar in wholelist[k]:
      if indchar in freqdict:
        print(f'Found same character:{indchar}')
        if indchar.isupper():
          sum += ord(indchar) - 38
        else:
          sum += ord(indchar) - 96
        itstime = True
        break
        
  i += 6

print(sum)