import math

piso = bloques = 1
total = 0
piramides = []

N = int(input())
for _ in range(N):
    H = int(input())
    bloques = H**2
    piramides.append(str(bloques))
    total += bloques
    # print((H-1)*espacio + ladrillo)
    # if H > 1:
    #     for x in range(1,H):
    #         piso +=2
    #         # print((H-x)*espacio + piso*ladrillo)
    #         bloques += piso
            
        # print(bloques)

print(total)
Elegido= max(piramides)
ladrillo = "*"
espacio=" "
H = int(math.sqrt(int(Elegido)))
print((H-1)*espacio + ladrillo)
if H > 1:
    for x in range(1,H):
        piso +=2
        print((H-x-1)*espacio + piso*ladrillo)
        bloques += piso
print(Elegido)