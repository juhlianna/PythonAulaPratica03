# b) Se dano é maior do que 10 e escudo é igual a 0, escreva: "Você está morto"
dano = int(input("Qual o valor do seu dano? "))
escudo = int(input("Qual o valor do seu escudo?"))
if (dano > 10 and escudo == 0):
    print("Você está morto!")