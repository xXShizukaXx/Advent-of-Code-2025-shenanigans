file = open("Day 4/D4 my data.txt", "r")
shelve = [line.rstrip() for line in file.readlines()]
shelves = list(shelve)

def create_margins(a):
    upper_and_lower='.'*len(a[0])
    a.insert(0, upper_and_lower)
    a.insert(len(a), upper_and_lower)

    for i in range(len(a)):
        a[i]= '.'+a[i]+'.'
    return a

def part_one(a):
    counter=0
    for y in range(1,len(a)-1):
        for x in range(1,len(a[y])-1):
            surrounded=0
            if a[y][x]=='@':
                #u means upper, l lower, l is left, r is right
                ul, u, ur, l, r, dl, d, dr= a[y-1][x-1], a[y-1][x], a[y-1][x+1],a[y][x-1],a[y][x+1],a[y+1][x-1],a[y+1][x],a[y+1][x+1]

                if ul=='@':surrounded+=1
                if u=='@':surrounded+=1
                if ur=='@':surrounded+=1
                if l=='@':surrounded+=1
                if r=='@':surrounded+=1
                if dl=='@':surrounded+=1
                if d=='@':surrounded+=1
                if dr=='@':surrounded+=1

                if surrounded<4: counter+=1
    return counter

def part_two(a, counter):
    carbon_copy=a.copy()
    check=False

    for y in range(1,len(a)-1):
        for x in range(1,len(a[y])-1):
            surrounded=0
            if a[y][x]=='@':
                #u means upper, l lower, l is left, r is right
                ul, u, ur, l, r, dl, d, dr= a[y-1][x-1], a[y-1][x], a[y-1][x+1],a[y][x-1],a[y][x+1],a[y+1][x-1],a[y+1][x],a[y+1][x+1]

                if ul=='@':surrounded+=1
                if u=='@':surrounded+=1
                if ur=='@':surrounded+=1
                if l=='@':surrounded+=1
                if r=='@':surrounded+=1
                if dl=='@':surrounded+=1
                if d=='@':surrounded+=1
                if dr=='@':surrounded+=1

                if surrounded<4: 
                    check=True
                    counter+=1
                    carbon_copy[y] = carbon_copy[y][:x] + '.' + carbon_copy[y][x+1:]

    if check: return part_two(carbon_copy, counter)
    else: return counter
    
number= part_two(create_margins(shelves),0)
print(number)
