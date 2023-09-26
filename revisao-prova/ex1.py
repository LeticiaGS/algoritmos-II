list_1 = []
list_2 = []
N = 3

print("\nLista 1:")
for i in range(N):
    list_1.append(int(input(f"Insira um número na posição [{i}]: ")))

print("\nLista 2:")
for i in range(N):
    list_2.append(int(input(f"Insira um número na posição [{i}]: ")))


list_1.reverse()
list_2.reverse()

print("\nLista 1 em sua ordem reversa: ")
print(list_1)

print("\nLista 2 em sua ordem reversa: ")
print(list_2)
