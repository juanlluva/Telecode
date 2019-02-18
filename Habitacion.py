line = str(input()).split()
N = int(line[0])
K = int(line[1])
print(N,K)
toAssing = []
habitaciones = []
current = 0
for _ in range(N):
	person = str(input()).split()
	toAssing.append(person[1])

for i in range(1,len(toAssing)-1)
