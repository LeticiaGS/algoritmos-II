#Ler 2 vetores, R de 5 elementos e S de 10 elementos, ambos de inteiros. Gere
#um vetor X que possua os elementos comuns a R e a S. Considere que no
#mesmo vetor não haverá números repetidos.

RMAX = 2
SMAX = 3
rVetor = []
sVetor = []
comumElVetor = []

print("\nVetor R:")
for i in range(RMAX):
    rVetor.append(int(input(f"Digite um valor inteiro para o indice [{i}]: ")))

print("\nVetor S:")
for i in range(SMAX):
    sVetor.append(int(input(f"Digite um valor inteiro para o indice [{i}]: ")))

for s in range(SMAX):
    for r in range(RMAX):
        if sVetor[s] == rVetor[r]:
            comumElVetor.append(rVetor[r])

for i in range(len(comumElVetor)):
    print(f"Os números em comum dos vetores são: [{i}]: [{comumElVetor[i]}]")
