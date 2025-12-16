#meeee? losing my mind...??? HAHAHAHAHAHAHAHAHAA-
import itertools
file= open("Day 6/D6 my data.txt", "r")
lines=[line.rstrip() for line in file.readlines()]

def transpose[T](arr: list[list[T]]): #yk the drill by now...shoutout to arkadios
    for row in arr: assert(len(row))==len(arr[0]) #check if all rows are, indeed, of the same length

    out=[]
    for j in range(len(arr[0])):
        out.append(list(map(lambda row: row[j], arr))) #columns are their own lists now

    return out

def list_to_int(lst):
    number= 0
    lst = list(filter(lambda c: c!="", lst))
    for i in range(len(lst)):
        number= number*10+lst[i]
    return number

def parse_part_1(l):
    i=0
    for line in l[:-1]:
        line=line.split()
        line=list(map(lambda line: [int(c) for c in line], line))
        l[i]=line
        i+=1
    l[-1]=l[-1].split()
    l=transpose(l)
    return l

def parse_part_2(l):
    values=parse_part_1(l)
    a=[]
    b=[]
    for numbers in values:
        first=len(numbers[0]) #precondition: the nth value WILL follow the pattern of the first three <-CAP!!!
        second=len(numbers[1])
        third=len(numbers[2])
        b.append(numbers[-1])
        if ((first>second) and (second>third)) or (first<second and second<=third):
            for digits in numbers[:-1]:
                digits.reverse()
        new = list(itertools.zip_longest(*numbers, fillvalue='')) 
        a.append(new)

    for numbers in a:
        for i in range(len(numbers)):
            numbers[i]= list_to_int(list(numbers[i])[:-1])
    return [a,b]

#ok....THIS IS THE MOMENT WE'VE BEEN WAITING FOR

def calc_part_2(l,m):
    sum=0
    for i in range(len(m)):
        temp=1
        if m[i]=='*':
            for j in range(len(l[i])):
                temp*=l[i][j]
            sum+=temp
        else: 
            for j in range(len(l[i])): sum+=l[i][j]
    return(sum)

        


a,b= parse_part_2(lines)
print(calc_part_2(a,b))

numbers= parsing_2(init)

print(calc(numbers, op))
