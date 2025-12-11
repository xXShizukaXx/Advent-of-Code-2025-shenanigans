file=open("Day 5/D5 test data.txt", "r")
lines:str=file.readlines()
fresh=set()
cut= lines.index("\n")
fresh_counter=0
not_rotten=0

list_of_fresh= lines[:cut-1]
test_if_fresh= lines[cut+1:]


for r in list_of_fresh:
        indicator= r.index("-")
        fresh_counter = int(r[:indicator])
        fresh.add(fresh_counter)
        final=int(r[(indicator+1):])

        for countup in range (fresh_counter, final):
            fresh_counter+=1
            fresh.add(fresh_counter)

#print(fresh)    

for i in range(len(test_if_fresh)):

    tested=int(test_if_fresh[i].rstrip())

    if tested in fresh:
         not_rotten+=1
print(not_rotten)
