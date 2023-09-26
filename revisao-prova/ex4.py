vetor = []
matriz = []

N = 3
M = 4

for i in range(N):
    vetor.append(int(input(f"Digite um valor para a posição [{i}]: ")))

for i in range(N):
    linha = []
    for j in range(M):
     linha.append(int(input(f"Digite um valor para a posição [{i}][{j}]: ")))
    matriz.append(linha)

print("\nAntes: ")
print(vetor)
for l in range(N):
   print(matriz[l])

for i in range(N):
   aux = vetor[i]
   vetor[i] = matriz[i][1]
   matriz[i][1] = aux

print("\nDepois: ")
print(vetor)
for l in range(N):
   print(matriz[l])