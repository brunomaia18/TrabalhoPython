sexo = input('Digite seu sexo F/M: ').upper()

while sexo != "":
    if sexo == "F" or sexo == "FEMININO":
        print('Seu sexo é F-Femino')
        break
    elif sexo == "M" or sexo == "MASCULINO":
        print("Seu sexo é M-Masculino")
        break
    else:
        print("Informe F/M")
        sexo = input('Digite seu sexo F/M: ').upper()