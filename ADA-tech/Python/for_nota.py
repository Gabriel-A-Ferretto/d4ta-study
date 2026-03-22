soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe sua nota {i}:'))
    soma = soma + nota


print(f'O resultado das suas três notas são {soma} : \n')
print(f'A media delas é -> {soma / 3}')
