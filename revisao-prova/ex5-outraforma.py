m1 = []
N = 3

for i in range(N):
    linha = []
    for j in range(N):
        linha.append(int(input(f"Insira um valor para a posição [{i}][{j}]: ")))
    m1.append(linha)

print(min(max(m1)))