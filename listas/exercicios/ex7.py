
x = []
y = []
dif = []

MAX = 3


print("\nPreencha o vetor X: ")
for i in range(MAX):
    x.append(int(input(f'Digite um valor para a posição: [{i}]')))

print("\nPreencha o vetor Y: ")
for i in range(MAX):
    y.append(int(input(f'Digite um valor para a posição: [{i}]')))


for xi in range(MAX):
    count = 0
    for yi in range(MAX):
        if (x[xi] == y[yi]):
            count+= 1
    if count == 0:
        dif.append(x[xi])

print(dif)