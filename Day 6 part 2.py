import itertools
from typing import List
file=open("Day 6/D6 test data.txt", "r")
lines= [line.rstrip() for line in file.readlines()]
sum=0


#does my parsing method still suck? Yes. But does it suck less than last week? Absolutely.
def arkadios_will_be_proud_of_me(l):
    i = 0
    for line in lines[:-1]:
            line= line.split(" ", len(line)) #converts strings into lists by splitting them by spaces
            line = list(filter(lambda c: c!="", line)) #gets rid of blank spaces
            line=list(map(lambda line: [str(int(c)) for c in line], line))  #turns every single sequence into its own list. for example, '123' becomes '1','2','3'
            lines[i]=line   #places new list of lists into the big list TM
            i+=1
    line= lines[len(lines)-1] #since last string consists of symbols, its parsing is done separately; but still following the same principle
    line= line.split(" ", len(line))
    line = list(filter(lambda c: c!="", line))
    lines[len(lines)-1]=line #add it to the big list

def transpose[T](arr: list[list[T]]): #shoutout to Arkadios (again) for teaching me this lol
    for row in arr: assert(len(row))==len(arr[0]) #check if all rows are, indeed, oof the same length

    out=[]
    for j in range(len(arr[0])):
        out.append(list(map(lambda row: row[j], arr))) #columns are their own lists now

    return out

#ok, now how to read numbers vertically? The solution is to zip it!
def parsing_part_two():
    b= transpose(lines) #honestly a game changer
    a=[]
    for operations in b:
        if (len(operations[1])==len(operations[2])) and len(operations[1])<=len(operations[0]) or (len(operations[0])<=len(operations[1]) and len(operations[1])<len(operations[2])):
            new = list(itertools.zip_longest(*operations))
        else:
            for values in operations[:-1]:
                values.reverse() #ofc! flip them!!
            new = list(itertools.zip_longest(*operations))
        a.append(new)
        print(a)

        return a
    
#what a ride... but now, it's time for the actual operation, don't you think? :)
#okay wait I am about to crash out...parsing_part_two() had been working a few minutes ago and now it doesn't sobbbbb

def calculation(a):
    number =0
    value=''

    """for k in a:
        for n in range(len(k)):
            if n==0:
                for m in range(len(k[0])-1):
                    value+=k[n][m]
            else:
                for m in range(len(k[n])):
                    value+=k[n][m]
            
            number= int(value)  """      


arkadios_will_be_proud_of_me(lines)                  
parsing_part_two()
calculation(parsing_part_two())
