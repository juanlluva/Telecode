import base64

N = int(input())
for _ in range(N):
	cod = input()
	print(base64.b32decode(bytearray(cod, 'ascii')).decode('utf-8'))