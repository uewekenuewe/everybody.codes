f = open('q1a', 'r')
lines = f.readlines()
result = 0
for l in lines:
    for x in l:
        if x == 'B':
            result += 1
        if x == 'C':
            result += 3
print('part1: ',result)

f = open('q1b', 'r')
lines = f.readlines()
result = 0
M = {
        'A' : 0,
        'x' : 0,
        'B' : 1,
        'C' : 3,
        'D' : 5,}
for l in lines:
    for x in range(0,len(l)-1,2):
        a,b = l[x:x+2]
        if a == 'x' or b == 'x':
            result += M[a] + M[b]
        else:
            result += M[a] + M[b] + 2
print('part2: ',result)

f = open('q1c', 'r')
#f = open('q1cex', 'r')
lines = f.readlines()
result = 0
M = {
        'A' : 0,
        'x' : 0,
        'B' : 1,
        'C' : 3,
        'D' : 5,}
for l in lines:
    for x in range(0,len(l)-2,3):
        a,b,c = l[x:x+3]
        monsterCount = 3-[a,b,c].count('x')
        if monsterCount == 3:
            result += 6
        else:
            if monsterCount == 2:
                result += 2
        result += M[a] + M[b] + M[c]
print('part3: ',result)

