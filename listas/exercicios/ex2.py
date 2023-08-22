#Faça um programa que preencha um vetor com 9 números inteiros, calcule e
#mostre os que são números primos e suas respectivas posições.

v = []
N = 3

for i in range(N):
    v.append(int(input(f"Digite um valor para a posição [{i}]: ")))

for i in range(N):
    cont = 0 
    # aqui se v[i] = 5, só irá até o 4. Por isso só validamos se cont = 1 para encontrar o primo. Se quiser fazer cont = 2 precisaria ser v[i]+1
    for x in range(1,v[i]): 
        if (v[i] % x == 0):
            cont += 1
    # validados o cont = 1 porq o num primo só pode ser div por 1 e por ele msm, no caso n chega até ele porq range(1,v[i])
    if cont == 1: 
        print(f'O número {v[i]} na posição {i} é impar.')