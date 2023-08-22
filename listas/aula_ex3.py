# Elabore um algoritmo que leia duas listas de 5 posições, após a leitura realizar a
# soma e imprima o resultado da soma entre as duas listas de inteiros.

x = [0,0,0,0,0]
y = [0,0,0,0,0]

N = 3

print("\nLista 1:")
for i in range (N):
    x[i] = int(input(f"Informe o valor do índice {i}: "))

print("\nLista 2:")
for i in range (N):
    y[i] = int(input(f"Informe o valor do índice {i}: "))

for i in range (N):
    print(f"\n O valor da soma entre as listas é [{i}]:[{x[i] + y[i]}]")