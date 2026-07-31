mult = int(input("Digite o número da Tabuada: "))
final = int(input("Digite o número que deve terminar a tabuada: "))

i = 1
while i <= final:
    print("{} x {} = {}".format(mult, i, mult*i))
    i += 1

