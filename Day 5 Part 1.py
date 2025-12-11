file=open("Day 5/D5 test data.txt", "r")
lines:str=file.readlines()
fresh=[]
cut= lines.index("\n")
fresh_counter=0

list_of_fresh= lines[:cut-1]
test_if_fresh= lines[cut+1:]

for r in list_of_fresh:
        indicator= r.index("-")
        fresh_counter_start = r[:indicator]
        fresh_counter_end = r[indicator+1:]
        ranges=(fresh_counter_start, fresh_counter_end)
        fresh.append(ranges)


for i in range(len(test_if_fresh)):
    for ranges in fresh:
        test=int(test_if_fresh[i])

        if int(ranges[0])<=test and test<=int(ranges[1]):
            fresh_counter+=1
            test_if_fresh.remove(test)
print(fresh_counter)
