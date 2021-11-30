dia = int(input("Informe o dia: "))
mes = int(input("Informe o mes: "))
ano = int(input("Informe o ano: "))


if dia <= 30 and mes <= 12 and dia >= 1 and mes >= 1 and ano >= 1000:
        print("Data válida!")
else:
    print("Data invalida!")
    

