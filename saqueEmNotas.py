saque = int(input("Digite o valor do saque: "))

cem = int(saque/100)
saque = saque - (cem*100)

cinquenta = int(saque/50)
saque = saque - (cinquenta*50)

dez = int(saque/10)
saque = saque - (dez*10)

cinco = int(saque/5)
saque = saque - (cinco*5)

um = saque

print(cem, "Notas de R$100")
print(cinquenta, "Notas de R$50")
print(dez, "Notas de R$10")
print(cinco, "Notas de R$5")
print(um, "Notas de R$1")