#meeee? losing my mind...??? HAHAHAHAHAHAHAHAHAA-
import itertools
file= open("Day 6/D6 my data.txt", "r")
lines= [line.replace("\n"," ") for line in file.readlines()]

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

#ok no IGNORE ALL OF THAT
#NEW APPROACH (shoutout to the subreddit)

def PLEASEWORK(l):
    sum=0
    operators=l[-1]+' '
    helper=[]
    t=1
    save=''
    for i in range(len(l[0])):
        temp=''
        for n in l[:-1]: 
            temp+= n[i]
            o=operators[i]
            if o=='*': save='*'
            elif o=='+': save='+'
        temp=temp.rstrip()
        if temp != '':
            number=int(temp)
            helper.append(number)
        else:
            if save=='+':
                for i in range(len(helper)):
                    sum+=helper[i]
            elif save=='*':
                temp=1
                for i in range(len(helper)):
                    temp*=helper[i]
                sum+=temp
            helper=[]
            save=''
    return sum

print(PLEASEWORK(lines))

#IT WORKS
#WAR IS OVER

