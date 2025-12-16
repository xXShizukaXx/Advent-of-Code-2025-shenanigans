#AoC D1 LET'S GOOOOO
file = open("Day 1/D1 test data.txt", "r")
lines = file.readlines()
counter = 0
sign=1 #move left or right
dial = 50 #isn't it neat?! :D

for i in range(len(lines)):
    bite = lines[i]
  
    if bite[0]=='L':
        sign = -1   #the shift while I rotate the dial
    elif bite[0]=='R':
        sign = 1

    shift = int(bite[1:])*sign

    marker = dial + shift
    dial = (marker)%100

    #for part 1 output:
    if dial == 0:
        counter +=1

print(counter)
