f = open("input.txt", "r")
sum = 0
for line in f:
  firsthalf, secondhalf = line[:len(line)//2], line[len(line)//2:]
  freqdict = {}
  for i in firsthalf:
    if i in freqdict:
      freqdict[i] += 1
    else:
      freqdict[i] = 0
  for i in secondhalf:
    if i in freqdict:
      print(f'Found same character:{i}')
      if i.isupper():
        sum += ord(i) - 38
      else:
        sum += ord(i) - 96
      break
# print(ord('a') - 96)
# print(ord('Z') - 38)
print(sum)