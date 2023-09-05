N = 2
vetorUm = []
vetorDois = []

print("Preencha os dados do vetor um:")
for i in range (N):
    vetorUm.append(int(input(f"Digite um valor inteiro para a posição: [{i}] do vetor:")))

print("\nPreencha os dados do vetor dois:")
for i in range (N):
    vetorDois.append(int(input(f"Digite um valor inteiro para a posição: [{i}] do vetor:")))


for i in range (N):
    print(vetorUm[i])
    print(vetorDois[i])
