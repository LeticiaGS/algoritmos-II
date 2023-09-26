
a = []
N = 10
count = 0

for i in range(N):
    a.append(int(input(f"Digite o {i + 1}° valor inteiro da lista: ")))

for i in range(N):
    if(a[i] < 0):
        count=+ 1
        print(f"\n{a[i]} é igual a zero. Armazenado na posição: [{i}]")
    elif (a[i] == 0):
        count=+ 1
        print(f"\n{a[i]} é menor do zero. Armazenado na posição: [{i}]")

if count == 0:
    print("\nNão há nenhum número menor ou igual a 0.")