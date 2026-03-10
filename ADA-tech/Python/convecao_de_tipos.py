#Conversaão de tipos

idade = '26'
print(type(idade))

idade_inteira = int(idade)
print(idade_inteira, type(idade_inteira))

idade_texto = input('Informe sua idade: ')
idade_inteira  = int(idade_texto)
print('Sua idade é: ', idade_inteira)

altura = float(input('Infome sua altura: '))
print(altura)