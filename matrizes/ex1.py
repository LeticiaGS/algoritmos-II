N = int(input("Informe N: "))

m1 = [] #lista
m2 = []
mR = []

print("\n Matriz 1: ")
for l in range(N):
    #ler linhas
    linha = []
    for c in range(N):
        #ler coluna da linha
        linha.append(int((input(f"Informe valor inteiro para a posição [{l}][{c}]: "))))
    #add a linha na m1
    m1.append(linha)

print("\n Matriz 2: ")
for l in range(N):
    #ler linhas
    linha = []
    for c in range(N):
        #ler coluna da linha
        linha.append(int((input(f"Informe valor inteiro para a posição [{l}][{c}]: "))))
    #add a linha na m1
    m2.append(linha)

#print(m1)
print(m2)

for l in range(N):
    linha = []
    for c in range(N):
        linha.append(m1[l][c] + m2[l][c])
    mR.append(linha)

for i in range(N):
    print(mR[i])
