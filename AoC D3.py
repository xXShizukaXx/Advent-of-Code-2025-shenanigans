file = open("Day 3/D3 my data.txt", "r")
lines = [line.rstrip() for line in file.readlines()]

banks = list(map(lambda line: [int(c) for c in line], lines))

def part_one(banks):
    output = 0

    for bank in banks:
        ones, tens = bank[0], bank[0]
        x=0
        y=0

        for i in range(len(bank)):
            if tens<bank[i]:
                tens=bank[i]
                x=i
            
        if x != (len(bank)-1):
            #tens = bank[x]
            y= x+1
            
            for k in range(y, len(bank)):
                if bank[y]<bank[k]:
                    y=k
            ones = bank[y]
        else:
            ones=bank[x]
            for l in range(x):
                if bank[y]<bank[l]:
                    y = l
            tens = bank[y]
        output += tens*10 + ones
    print(output)

def calc(number,exp):
    return number*(10**exp)

def part_two_for_the_nth_time(banks):
 sum=0
 for bank in banks:
    pointer=0
    x=0
    number=0
    search=bank
    for i in range(11,-1,-1):
        y=len(bank)-i
        for j in range(x,y):
            if pointer<search[j]:
                pointer=search[j]
                x=j+1
        number+=calc(pointer, i)
        pointer=0
    print(number)
    sum+=number
 return sum
print(part_two_for_the_nth_time(banks))
#start from...behind?
