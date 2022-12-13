# Open file 
f = open("input1.txt", "r")

# Initialize dictionary to hold elf calories
# Set first elf to 0 so we don't have to worry about key errors
elfdict = {0:0}
curelf = 0

# Iterate through each line and add calories per elf
for calories in f:
  # Move on to next elf and initialize calories to 0 if newline is detected
  if calories == '\n':
    curelf += 1
    elfdict[curelf] = 0
    continue
  elfdict[curelf] += int(calories)
print(elfdict)
print(max(elfdict.values()))
  