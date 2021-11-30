produto1 = float(input("Digite o valor do primeiro produto:"))
produto2 = float(input("Digite o valor do segundo produto:"))
produto3 = float(input("Digite o valor do terceiro produto:"))


if produto1 < produto2:
    if produto1 < produto3:
        print("Você tem que comprar o primeiro produto!")

if produto2 < produto1:
    if produto2 < produto3:
        print("Voce tem que comprar o segundo produto!")

if produto3 < produto1:
    if produto3 < produto2:
        print("Voce tem que comprar o terceiro produto!")