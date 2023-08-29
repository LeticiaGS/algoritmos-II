#Ler um vetor R de 5 elementos, inteiros, contendo o resultado da LOTO. A seguir ler
#um vetor A de 10 elementos inteiros contendo uma aposta. A seguir imprima quantos
#pontos fez o apostador
import random

rMAX = 5
aMAX = 10
loto = []
aposta = []
cont = 0

for i in range(rMAX):
    loto.append(random.randint(1,50))

print(loto)

for i in range(aMAX):
    aposta.append(int(input(f"Insira {i+1}º número da sua aposta: ")))

for a in range(aMAX):
    for r in range(rMAX):
        if aposta[a] == loto[r]:
            cont += 1

if cont == 5:
    print("\nVOCÊ GANHOU NA LOTOOOOOO!!!")
elif cont == 0:
    print("\nNão foi dessa vez! :/ Você não acertou nennhum número.")
else:
    print(f"\nVocê fez {cont} pontos!")