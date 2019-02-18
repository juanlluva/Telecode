import math

N = int(input())
for _ in range(N):
	screen = str(input()).split()
	resalto= int(screen[2])
	resancho= int(screen[1])
	res = float(screen[0])
	alpha = math.atan2(resalto,resancho)
	ancho = res*25.4*(math.cos(alpha))
	alto = res*25.4*(math.sin(alpha))
	print("" + str(int(ancho)) + " " + str(int(alto)))
