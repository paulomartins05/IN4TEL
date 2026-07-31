palavra = input("Digite uma palavra: ")

palavraMaiuscula = palavra.upper()

contadorVogais = 0

for letra in palavraMaiuscula:
    print(letra)

    if letra in "AEIOU":
        contadorVogais += 1

print("Vogais: {}".format(contadorVogais))

if 'A' in palavraMaiuscula:
    print("A letra 'A' está presente")
else:
    print("A letra 'A' NÃO está presente")