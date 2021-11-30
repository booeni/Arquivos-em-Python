morango = int(input(" Quantos KG de morango voce quer comprar? "))
maca = int(input(" Quantos KG de maca voce quer comprar? "))

precoMorango = 2.50
precoMaca = 1.80
pesoMorango = morango
pesoMaca = maca
pesoTotal = pesoMorango + pesoMaca
valorTotal = ( morango * precoMorango )  + ( maca * precoMaca )

if pesoMorango > 5:
    precoMorango = 2.20

if pesoMaca > 5:
    precoMaca = 1.50

if pesoTotal > 8 or valorTotal > 25:
    valorTotal = valorTotal - (valorTotal * 0.1)

print("O valor a ser pago é R$:","{:.2f}".format(valorTotal), "reais" )