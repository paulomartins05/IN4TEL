dist = float(input("Digite a distancia em km: "))

if dist <= 200:
    print("O valor da viagem sera: R${}".format(dist*0.5))
else:
    print("O valor da viagem sera: R${}".format(dist*0.45))