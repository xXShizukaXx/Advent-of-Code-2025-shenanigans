file=open("Day 12/D12 my data.txt", "r")
lines=[line.rstrip() for line in file.readlines()]
presents_area=7
i=0
yes=0
for line in lines:
    line= line.split(" ", len(line))
    lines[i]=line
    i+=1

for line in lines:
    presents=0
    area=line[0]
    a=area.split('x', 1)
    a[1]=a[1][:len(a[1])-1]
    print(a[1])
    size= int(a[0])*int(a[1])

    for j in range(1, len(line)):
        presents+=int(line[j])
    presents=presents*presents_area

    if presents<=size:
        yes+=1
print(yes)






