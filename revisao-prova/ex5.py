m1 = []
N = 5
max = 0
menor = 999999999999
linhaMax = 0


for i in range(N):
    linha = []
    for j in range(N):
        linha.append(int(input(f"Insira um valor para a posição [{i}][{j}]: ")))
    m1.append(linha)

for i in range(N):
    for j in range(N):
        if m1[i][j] > max:
            max = m1[i][j]
            linhaMax = i

print("linha max: ",linhaMax)

for i in range(N):
    if m1[linhaMax][i] < menor :
      menor = m1[linhaMax][i]

print(menor)