nome = input("Qual o seu nome? ")

print(nome.lower())
print(nome.upper())

nomeSemEspacos = nome.replace(" ", "")
print(len(nomeSemEspacos))

parteDoNome = nome.split()
ultimoNome = parteDoNome[-1]
nameNovo = nome.replace(ultimoNome, "do Inatel")
print(nameNovo)
