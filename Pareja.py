import math
def FindAllDivisors(x):
    divList = []
    # y = 1
    # while y <= math.sqrt(x):
    #     if x % y == 0:
    #         divList.append(y)
    #         divList.append(int(x / y))
    #     y += 1
    for y in range(1,int(math.sqrt(x)+1)):
        if x % y == 0:
            divList.append((y + x/y, y, x/y))
    return divList

suma = {}
N = int(input())
for _ in range(N):
    Incognita = int(input())
    divisores = FindAllDivisors(Incognita)

    # for i in range(1,len(divisores)):
    #     for j in range(i,len(divisores)):
    #         if i*j == Incognita :
    #             suma[i]=(i+j)
    triple = min(divisores, key = lambda x: x[0])
    # for i,sumado in suma.items():
 #        if sumado == elegido:
 #            aux = i
    print(str(triple[1]) + " " + str(triple[2]))

