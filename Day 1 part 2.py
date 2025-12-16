#this will NOT look pretty but let's give it a try
file = open("Day 1/D1 my data.txt", "r")
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

    for j in range(abs(shift)):
        if shift>0:
            dial+=1
        elif shift<0: dial-=1
        elif shift==0:break

        if dial<0:
            dial=99

        elif dial>99:
            dial=0

        if dial==0: counter+=1
print(counter)
