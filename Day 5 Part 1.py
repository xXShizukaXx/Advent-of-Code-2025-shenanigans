file=open("Day 5/D5 test data.txt", "r")
lines:str=file.readlines()
fresh=[]
cut= lines.index("\n")
fresh_counter=0
not_rotten=0

#banks = list(map(lambda line: [int(c) for c in line], lines))

list_of_fresh= lines[:cut-1]
test_if_fresh= lines[cut+1:]

def converting(list):
     lambda list: [i.rstrip() for i in list]
     lambda list: [int(i) for i in list]

converting(list_of_fresh)
converting(test_if_fresh)


for r in list_of_fresh:
        indicator= r.index("-")
        fresh_counter_start = r[:indicator]
        fresh_counter_end = r[indicator+1:]
        ranges=(fresh_counter_start, fresh_counter_end)
        fresh.append(ranges)

for ranges in fresh:
       for i in range(len(test_if_fresh)):
            test=int(test_if_fresh[i])

            if int(ranges[0])<=test and test<=int(ranges[1]):
                  fresh_counter+=1
print(fresh_counter)

