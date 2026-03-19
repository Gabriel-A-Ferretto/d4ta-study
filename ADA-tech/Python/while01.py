print('Descubra o número ->')

numero_sorteado = 15 

numero_escolhido = input('Informe um número entre 1 e 20: ')

# if numero_sorteado ==  numero_escolhido:
#     print('Você acertou!')
# else:
#     print('Vocẽ errou!')

while numero_escolhido != numero_sorteado:
    print('Você errou o número, tente novamente...')

    numero_escolhido = int(input('Informe um número entre 1 e 20: '))

frase = 'Parabens você acertou'
print(frase)