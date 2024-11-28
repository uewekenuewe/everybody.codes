a = open("q4a","r")
lines = a.readlines()
lines = [int(l) for l in lines]

ansa = 0
ansb = 0
ansc = 0
for l in lines:
    ansa += abs(min(lines) - l)

b = open("q4b","r")
lines = b.readlines()
lines = [int(l) for l in lines]
for l in lines:
    ansb += abs(min(lines) - l)


c = open("q4c","r")
lines = c.readlines()
lines = [int(l) for l in lines]
results = []
for x in lines:
    currMin = 0
    for l in lines:
        currMin += abs(x - l)
    results.append(currMin)
ansc = min(results)





print("Quest 4 A: ",ansa)
print("Quest 4 B: ",ansb)
print("Quest 4 C: ",ansc)
