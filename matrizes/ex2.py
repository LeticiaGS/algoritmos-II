import numpy as np

N = 10

M1 = np.zeros((N, N))
print(M1)

for l in range(N):
    for c in range(N):
      #  print(l)
      M1[l][c] = l  
# M1[l][c] = int(input(f"Informe valor para lin {l}, col {c}:")
print(M1)

line2 = np.zeros((N))
line5 = np.zeros((N))
line2 = M1[2]
line5 = M1[5]
print(line2)
M1[2] = M1[8]
M1[5] = M1[9]
M1[8] = line2
M1[9] = line5
print(line2)
#for i in range(N):
#    aux = M1[2][i]
#    M1[2][i] = M1[8][i]
#    M1[8][i] = aux
    
#for i in range(N):
#    aux = M1[5][i]
#    M1[5][i] = M1[i][9]
#    M1[i][9] = aux

print(M1)