nota1 = float(input("Qual e o valor da primeira nota parcial? "))

nota2 = float(input("Qual e o valor da segunda nota parcial? "))

media = (nota1 + nota2) / 2

print(" A sua média foi de: ", media)

if media >= 9 and media < 10:
    print(" O seu conceito de nota foi A")

if media >= 7.5 and media < 9:
    print(" O seu conceito de nota foi B")

if media >= 6 and media < 7.5:
    print(" O seu conceito de nota foi C")

if media >= 4 and media < 6:
    print(" O seu conceito de nota foi D")

if media > 0 and media < 4:
    print(" O seu conceito de nota foi E")

if media > 6 and media <= 10:
    print(" Você foi APROVADO!")

else:
    print(" Você foi reprovado!")

