import numpy as np
a = open("q6ex","r")
a = open("q6","r")
lines = a.readlines()
ansa = 0
ansb = 0
ansc = 0

T = {}
for l in lines:
    spl = l.replace("\n","").split(":")
    T[spl[0]] = spl[1].split(",")

q = [["RR"]]
routes = []
result = []
while(len(q) > 0):
    first = q[0]
    q = q[1:] 
    if first[-1] == "@":
        result.append("".join(first))
    if first[-1] in T.keys():
        for x in T[first[-1]]:
            ele = first + [x]
            q.append(ele)

result2 = {}
for r in result:
    if len(r) in result2.keys():
        result2[len(r)].append(r)
    else:
        result2[len(r)] = [r] 

for r in result2:
    if len(result2[r]) == 1:
        ansa = result2[r]
        break

print(ansa)

a = open("q6b","r")
lines = a.readlines()
ansb = 0

T = {}
for l in lines:
    spl = l.replace("\n","").split(":")
    T[spl[0]] = spl[1].split(",")

q = [["RR"]]
routes = []
result = []
while(len(q) > 0):
    first = q[0]
    q = q[1:] 
    if first[-1] == "@":
        result.append((first))
    if first[-1] in T.keys():
        for x in T[first[-1]]:
            ele = first + [x]
            q.append(ele)

for i,r in enumerate(result):
    result[i] = [x[0] for x in r]

result2 = {}
for r in result:
    if len(r) in result2.keys():
        result2[len(r)].append(r)
    else:
        result2[len(r)] = [r] 

for r in result2:
    if len(result2[r]) == 1:
        ansb = result2[r]
        break

print("".join(ansb[0]))


a = open("q6c","r")
lines = a.readlines()
ansc = 0

T = {}
for l in lines:
    spl = l.replace("\n","").split(":")
    T[spl[0]] = spl[1].split(",")

q = [["RR"]]
routes = []
result = {}
checked = {}
ansc = []
i = 0
while(i < 10000):
    first = q[0]
    q = q[1:] 
    if first[-1] == "@":
        if len(first) not in result.keys() and len(first) not in checked.keys():
            result[len(first)] = first
        else:
            if len(first) in result.keys():
                del result[len(first)] 
            if len(first) not in checked.keys():
                checked[len(first)] = 1 
    if first[-1] in T.keys():
        for x in T[first[-1]]:
            ele = first + [x]
            q.append(ele)
    i+=1

for x in result:
    ansc = (result[x])
ansc = [x[0] for x in ansc]
print("".join(ansc))
