verificar = input("Digite uma letra pra saber se é vogal ou consoante: ").lower()
lista =["a","e","i","o","u"]

if verificar == lista[0] or verificar == lista[1] or verificar == lista[2] or verificar == lista[3] or verificar == lista[4]:
    print("Você acabou de digitar uma VOGAL")
else:
    print("Você acabou de digitar uma Consoante")