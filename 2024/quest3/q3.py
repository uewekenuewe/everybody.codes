import sys
import numpy as np
np.set_printoptions(threshold = sys.maxsize)
np.set_printoptions(linewidth=99999)

f = open('q3a','r')
lines = f.readlines()
mat = []
for i,l in enumerate(lines):
    lines[i] = l.replace("\n","")
    ll = [1 if x == '#' else 0 for x in lines[i]]
    mat.append([x for x in ll])
mat = np.array(mat)

ansa =  np.count_nonzero(mat == 1)

DD = [(1,0),(0,1),(-1,0),(0,-1)]
found = True
currentLevel = 1
while(found):
    found = False
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if mat[x][y] == currentLevel:
                levelup = 0
                for d in DD:
                    dx = x + d[0]
                    dy = y + d[1]
                    if 0<=dx<len(mat) and 0<=dy<len(mat[x]) and mat[dx][dy] >= currentLevel:
                        levelup += 1
                if levelup == 4:
                    mat[x][y] = mat[x][y]+1
                    found = True
    if found:
        currentLevel += 1
        ansa += np.count_nonzero(mat == currentLevel)

print("Quest 3 A: ", ansa)

f = open('q3b','r')
lines = f.readlines()
mat = []
for i,l in enumerate(lines):
    lines[i] = l.replace("\n","")
    ll = [1 if x == '#' else 0 for x in lines[i]]
    mat.append([x for x in ll])
mat = np.array(mat)

ansb = np.count_nonzero(mat == 1)
DD = [(1,0),(0,1),(-1,0),(0,-1)]
found = True
currentLevel = 1
while(found):
    found = False
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if mat[x][y] == currentLevel:
                levelup = 0
                for d in DD:
                    dx = x + d[0]
                    dy = y + d[1]
                    if 0<=dx<len(mat) and 0<=dy<len(mat[x]) and mat[dx][dy] >= currentLevel:
                        levelup += 1
                if levelup == 4:
                    mat[x][y] = mat[x][y]+1
                    found = True
    if found:
        currentLevel += 1
        ansb += np.count_nonzero(mat == currentLevel)



print("Quest 3 B: ", ansb)


f = open('q3c','r')
lines = f.readlines()
mat = []
for i,l in enumerate(lines):
    lines[i] = l.replace("\n","")
    ll = [1 if x == '#' else 0 for x in lines[i]]
    mat.append([x for x in ll])
mat = np.array(mat)

ansc = np.count_nonzero(mat == 1)
DD = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
found = True
currentLevel = 1
while(found):
    found = False
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if mat[x][y] == currentLevel:
                levelup = 0
                for d in DD:
                    dx = x + d[0]
                    dy = y + d[1]
                    if 0<=dx<len(mat) and 0<=dy<len(mat[x]) and mat[dx][dy] >= currentLevel:
                        levelup += 1
                if levelup == len(DD):
                    mat[x][y] = mat[x][y]+1
                    found = True
    if found:
        currentLevel += 1
        ansc += np.count_nonzero(mat == currentLevel)


print("Quest 3 C: ", ansc)
