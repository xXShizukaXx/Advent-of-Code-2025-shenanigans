#deep breath in...deep breath out
#stupid octopus math...
#but it's okay...NEVER BACK DOWN; NEVER WHAT??
#okay...I've literally got everything I need...it's just a hot mess and THAT'S why it doesn't work
import itertools
import math
file=open("Day 6/D6 test data.txt", "r")
lines= [line.rstrip() for line in file.readlines()]
sum=0
#this code....is a HOT mess
#but that's okay...because it's MY hot mess
#step...by...step

def transpose[T](arr: list[list[T]]): #shoutout to Arkadios (again) for teaching me this lol
    for row in arr[:-1]: assert(len(row))==len(arr[0]) #check if all rows are, indeed, oof the same length

    out=[]
    for j in range(len(arr[0])):
        out.append(list(map(lambda row: row[j], arr))) #columns are their own lists now

    return out

def parsing_1(l): #yes, this used to be arkadios_will_be_proud_of_me() sorry arkadios I need an overview sobbbb
    i=0
    for line in l[:-1]:
        line= line.split(" ") #converts strings into lists by splitting them by spaces
        line = list(filter(lambda c: c!="", line)) #gets rid of blank spaces
        line=list(map(lambda line: [str(int(c)) for c in line], line))  #turns every single sequence into its own list. for example, '123' becomes '1','2','3'
        l[i]=line   #places new list of lists into the big list TM
        i+=1
    operators= l[(len(l)-1)]
    l.remove(operators) #remove from the big list
    operators=operators.split(" ") #since last string consists of symbols, its parsing is done separately; but still following the same principle
    operators = list(filter(lambda c: c!="", operators))
    return [l, operators] #ok I got my values...NEXT

def parsing_2(m): #the second part focuses on the actual transposing yada yada
    b=transpose(m)
    a=[]

    for operations in b:
        if (len(operations[1])==len(operations[2])) and len(operations[1])<=len(operations[0]) or (len(operations[0])<=len(operations[1]) and len(operations[1])<len(operations[2])):
            new = list(itertools.zip_longest(*operations, fillvalue=''))
        else:
             for values in operations[:-1]:
                  values.reverse() #ofc! flip them!!
             new = list(itertools.zip_longest(*operations, fillvalue=''))
        a.append(new)
    
    for element in a:
            i=0
            for tup in element:
                my_number=''
                for j in range (len(tup)): my_number+= tup[j]
                my_number=int(my_number)
                element[i]=my_number
                i+=1
                #print(element)
    return a

def calc(numbers, operators):
    sum=0
    for i in range(len(operators)):
            temp=0
            if operators[i]=='+':
                for j in range(len(numbers[i])): temp+=numbers[i][j]
            else:
                temp=math.prod(numbers[i])
            sum+=temp
    return sum
                 

init= parsing_1(lines.copy())[0]
op=parsing_1(lines.copy())[1]
numbers= parsing_2(init)

print(calc(numbers, op))
