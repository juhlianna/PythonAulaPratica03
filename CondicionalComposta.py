''' Condicional composta
Traduza as afirmações a seguir para
condicionais em Python:
a) Se ano é divisível por 4, escreva: “Pode ser
um ano bissexto”. Caso contrário, escreva:
“Definitivamente não é um ano bissexto
b) Se ambas as variáveis booleanas cima e
baixo forem True , escreva: “Decida se!”,
caso contrário, escreva: “Você escolheu
um caminho!”'''

ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')