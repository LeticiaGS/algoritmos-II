carros = ['Vectra','Gol','Uno','Fusca',"HB20"]
kmPorL = [8, 12.2, 10, 15, 11, 9]

maior = 0
pos = -1

for i in range (len(kmPorL)):
    if (kmPorL[i] > maior):
        maior = kmPorL[i]
        pos = i


print(f'O carro que faz mais Km por litro é o {carros[pos]} fazendo {maior}km por litro.')