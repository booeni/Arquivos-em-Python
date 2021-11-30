print("Responda as perguntas com sim ou nao")
pergunta1 = input(" Telefonou para a vítima? ")
pergunta2 = input(" Esteve no local do crime? ")
pergunta3 = input(" Mora perto da vítima? ")
pergunta4 = input(" Devia para a vítima? ")
pergunta5 = input(" Ja trabalhou com a vítima? ")
perguntas = 0
sim = 1
nao = 0

if pergunta1 == "sim":
    perguntas = perguntas + 1

if pergunta2 == "sim":
    perguntas = perguntas + 1

if pergunta3 == "sim":
    perguntas = perguntas + 1

if pergunta4 == "sim":
    perguntas = perguntas + 1

if pergunta5 == "sim":
    perguntas = perguntas + 1

else:
    perguntas = perguntas + 0

if perguntas < 2:
    print("Voce foi considerado como inocente!")

elif perguntas == 2:
    print("Voce foi considerado como Suspeito!")

if perguntas == 3 or perguntas == 4:
    print("Voce foi considerado como Cumplice!")

if perguntas == 5:
    print("Voce foi considerado como Assassino")

    







