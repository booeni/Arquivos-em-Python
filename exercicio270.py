morango = int(input("Quantos KG de morango você quer comprar? "))
maca = int(input("Quantos KG de maçã você quer comprar? "))

precoMorango = 2.50 
precoMaca = 1.80 
pesoTotal = morango + maca
valorMorango = (morango * precoMorango)
valorMaca = (maca * precoMaca)
valorTotal = (valorMorango + valorMaca)

if morango > 5:
    precoMorango = 2.20 * morango

if maca > 5:
    precoMaca = 1.50 * maca

if valorTotal > 25 or pesoTotal > 8:
    valorTotal = valorTotal - (valorTotal * 0.1)

print("O valor a ser pago é R$:","{:.2f}".format(valorTotal), "reais" )
