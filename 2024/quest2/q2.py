import sys
import numpy as np

f = open(sys.argv[1],'r')
lines = f.readlines()
for i,l in enumerate(lines):
    lines[i] = l.replace("\n","")

words = []
inp = lines[2]


ansA = 0
words = lines[0].replace('\n','').split(':')[1].split(',')
for w in words:
    ansA += inp.count(w)

print('Quest 2 A: ', ansA)

def countWords(line, words):
    result = 0
    toAdd = [0 for _ in range(len(line))]
    for w in words:
        for x in range(len(line)-len(w)+1):
            if line[x:x+len(w)] == w or line[x:x+len(w)] == w[::-1]:
                for y in range(x,x+len(w)):
                    toAdd[y] = 1

    result += toAdd.count(1)

    return result



ansB = 0 
for l in lines[2:]:
    l = l.replace('\n','')
    ansB += countWords(l,words)
print('Quest 2 B: ', ansB)


def checkLineBin(line,word,loop=False):
    result = [0 for _ in line]
    if loop == False:
        for i in range(len(line)-len(word)+1):
            if line[i:i+len(word)] == word:
                for j in range(i,i+len(word)):
                    result[j] = 1
    else:
        for i in range(len(line)-len(word)+1):
            if line[i:i+len(word)] == word:
                for j in range(i,i+len(word)):
                    result[j] = 1
        for i in range(len(line)-len(word)+1,len(line)):
            ll = abs(len(line[i:])-len(word))
            if line[i:] + line[:ll] == word:
                for x in range(ll):
                    result[x] = 1
                for x in range(i,len(result)):
                    result[x] = 1

    return result


ansC = 0
mat = []
matcheck = []
for l in lines[2:]:
    l = l.replace('\n','')
    mat.append([x for x in l])
    matcheck.append([0 for x in l])

mat = np.array(mat)
ansC = np.sum(matcheck == 1) 


matcheck = np.array(matcheck)
for i,x in enumerate(lines[2:]):
    for w in words:
        checkbin = checkLineBin(x,w,True)
        matcheck[i] = [matcheck[i][y] or checkbin[y] for y in range(len(matcheck[i]))]
        wrev = w[::-1]
        checkbin = checkLineBin(x,wrev,True)
        matcheck[i] = [matcheck[i][y] or checkbin[y] for y in range(len(matcheck[i]))]

for x in range(len(mat[0])):
    ll = "".join(mat[ : , x])
    for w in words:
        checkbin = checkLineBin(ll,w,False)
        matcheck[:, x] = [matcheck[y][x] or checkbin[y] for y in range(len(matcheck[:, x]))]
        wrev = w[::-1]
        checkbin = checkLineBin(ll,wrev,False)
        matcheck[:, x] = [matcheck[y][x] or checkbin[y] for y in range(len(matcheck[:, x]))]

print(matcheck)
ansC = np.count_nonzero(matcheck==1)
print('Quest 2 C: ', ansC)
