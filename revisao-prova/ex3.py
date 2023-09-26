list_a = []
N=3

maiorValor = 0
menorValor = 999999999999999999999
maiorValorPos = 0
menorValorPos = 0


for i in range(N):
    list_a.append(float(input("Digite um valor: ")))

for i in range(N):
    if(list_a[i] > maiorValor):
        maiorValor = list_a[i]
        maiorValorPos = i
    
    if(list_a[i] < menorValor):
        menorValor = list_a[i]
        menorValorPos = i

print(f"O menor valor inserido foi: {menorValor} na posição: [{menorValorPos}]")
print(f"O maior valor inserido foi: {maiorValor} na posição: [{maiorValorPos}]")