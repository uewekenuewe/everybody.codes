import numpy as np
a = open("q5bex","r")
a = open("q5b","r")
a = open("q5c","r")
a = open("q5cex","r")
lines = a.readlines()
lines = [[int(x) for x in l.split()] for l in lines]
ansa = 0
ansb = 0
ansc = 0

m = []
for x in lines[0]:
    m.append([])

for l in lines:
    for i,x in enumerate(l): 
        m[i].append(x)

counter = {}

def clap(mm,i):
    ind = i%len(mm)
    first = mm[ind][0]
    mm[ind] = mm[ind][1:]

    ind2 = (ind + 1 ) % len(mm)
    pos = (first) % (len(mm[ind2]) * 2) 
    
    if (pos-1) >= len(mm[ind2]):
        pos %= len(mm[ind2])
        mm[ind2].insert(pos+1,first)
    else:
        mm[ind2].insert(pos-1,first)

    result = ""
    for x in mm:
    #    print(x)
        result += str(x[0])

    return (result,mm)

def clap2(mm,i):
    ind = i%len(mm)
    first = mm[ind][0]
    mm[ind] = mm[ind][1:]

    ind2 = (ind + 1 ) % len(mm)

    if first >= len(mm[ind2]):
        mm[ind2].insert(len(mm[ind])-2,first)
    else:
        mm[ind2].insert(first-1,first)

    result = ""
    for x in mm:
        result += str(x[0])

    return (result,mm)


#for i in range(10):
i = 0
utest =      [6345 ,  
     6245 , 
     6285 ,  
     5284 ,  
     6584 ,  
     6254 ,  
     6285 ,  
     5284 , 
     6584 ,   
    6254  ]  

#while(ansb == 0):
while(True):
    result, xo = clap(m,i)
    ansc = max(ansc,int(result))

#    if result in counter.keys():
#        counter[result] += 1 
#        if counter[result] == 2024:
#            ansb = (i+1) * int(result)
#    else: 
#        counter[result] = 1
    m = xo
    i+=1 
    print(i,ansc, result)

print("Quest 5 B: " ,ansb)
print("Quest 5 C: " ,ansc)
