file=open("Day 5/D5 my data.txt", "r")
lines:str=file.readlines()
fresh=[]
cut= lines.index("\n")
fresh_counter=0

list_of_fresh= lines[:cut]
test_if_fresh= lines[cut+1:]

for r in list_of_fresh:
        indicator= r.index("-")
        fresh_counter_start = r[:indicator]
        fresh_counter_end = r[indicator+1:]
        ranges=[int(fresh_counter_start), int(fresh_counter_end)]
        fresh.append(ranges)

def part_one():
    for i in range(len(test_if_fresh)):
        for ranges in fresh:
            test=int(test_if_fresh[i])

            if int(ranges[0])<=test and test<=int(ranges[1]):
                fresh_counter+=1
                break
    print(fresh_counter)

def sort(a):
     indicator=True
     while indicator:
          indicator=False
          for i in range(len(a)-1):
               if a[i+1][0] < a[i][0]:
                    temp= a[i]
                    a[i]= a[i+1]
                    a[i+1]=temp
                    indicator=True
               elif a[i+1][0]==a[i][0] and a[i+1][1]<a[i][1]:
                    temp= a[i]
                    a[i]= a[i+1]
                    a[i+1]=temp
                    indicator=True

     return a
def part_two(a):
    list= sort(a)
    indicator=True
    counter=0
    while indicator:
        indicator=False
        for i in range(1, len(list)):
                if list[i][0]<=list[i-1][1]:
                        list[i][0]=list[i-1][1]+1
                        if list[i][1]<=list[i-1][1]: 
                            list.pop(i)
                            list=sort(list)
                            indicator=True
                            break
    for k in range(len(list)):
         counter+=1+list[k][1]-list[k][0]
    return counter
