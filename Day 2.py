#day 2! on...day 18...but we don't talk about that
#precondition: any list with an odd length is valid automatically; as it cannot have the same number of equal characters on each side
#I'd also like to try out functions...the right way!
#ok enough yapping I should just start
file = open("Day 2/D2 my data.txt", "r")
lines = [line.split(',') for line in file.readlines()]
a=lines[0]

print(lines)
def part_one(little_array):
    counter=0
    for ranges in little_array:
        ranges=ranges.split('-')
        for i in range(int(ranges[0]), int(ranges[1])+1):
            test=str(i)
            if len(test)%2==0:
                first=test[len(test)//2:]
                second=test[:len(test)//2]
                flag= True
                if first != second: flag= False
                if flag: counter+= i
    return counter
#print(part_one(lines[0]))

#yay it works!
#but also, part two throws my part one precondition into the nether...that's quite unfortunate
#okay new precondition: odd length leads to sequences of either the same number or the same 3 numbers (if divisible by 3)

def part_two(little_array):
    counter=0
    for ranges in little_array:
        ranges=ranges.split('-')

        for i in range(int(ranges[0]), int(ranges[1])+1):
            flag=True
            test=str(i)
            if len(test)%2==0 and len(test)>2:
                first=test[len(test)//2:]
                last=test[:len(test)//2]
                if first != last:
                    heh=test[:2]
                    for j in range(2, len(test)-1, 2):
                        if heh != test[j:j+2]: flag=False
            
            elif len(test)%3==0 and len(test)>3:
                nom=test[:3]
                for k in range(3, len(test)-2, 3):
                    huh= test[k:k+3]
                    if nom != huh: flag=False
            else:
                for l in range(len(test)-1):
                    if test[l] != test[l+1]: flag=False
                if len(test)==1: flag=False
            if flag: 
                #print(i)
                counter+=i
    return counter


print(part_two(a))


import timeit
a = '''
from math import sqrt
def example():
    mylist = [sqrt(x) for x in range(100)]
'''
t = timeit.timeit(a, number=1000000) * 1e3
print(round(t, 3), "ms")
