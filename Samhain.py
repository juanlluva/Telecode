pocion = {}
shouldWorry = []
N = int(input())
for _ in range(N):
    line = input().split()
    action = line[0]
    item = line[1]
    if action == 'a':
        if item in pocion.keys():
            pocion[item] +=1
        else:
            pocion[item] = 1
    elif action == 'q':
        pocion[item] -=1
    elif action == 'b':
        if item in pocion.keys():
            if pocion[item] > 0:
                shouldWorry.append(str(_))

print(' '.join(shouldWorry))