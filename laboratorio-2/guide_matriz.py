#matriz 3x3
m1 = [[8, 'a', -6],
      [12,7,'4'],
      [-11,3,21]]

matrix_length = len(m1) #con len podemos saber el tama;o del elemento, en este caso es 3.

for i in range(matrix_length):
    for j in range(len(m1[i])):
        print(m1[i][j])

