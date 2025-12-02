print("")
print("Bem-Vindo! / Welcome!")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("Escolha uma opção / Choose an option")
print("")
print("1 - Português / Portuguese")
print("2 - Inglês / English")
print("")

Lingua = int(input("Digite aqui / Type here: "))

if Lingua == 1:

## Cadastro:
    Nota_1 = int(input('Digite a nota da 1ª prova: '))
    Nota_2 = int(input('Digite a nota da 2ª prova: '))
    Nota_3 = int(input('Digite a nota da 3ª prova: '))
    Nota_4 = int(input('Digite a nota da 4ª prova: '))

    lista = [Nota_1, Nota_2, Nota_3, Nota_4]

    ## Cálculo da média:
    soma = (Nota_1 + Nota_2 + Nota_3 + Nota_4)
    média = (soma/4)

    ## Relatório
    print('-----------------------------------------------------')
    print('Resultados')
    print('')
    print('Soma das notas: ', soma)
    print ("Notas atribuidas no sistema: ", lista)
    print('')
    print('Sua média é: ', média)

    ## Determinação da situação
    if média >= 7 and média <=10:
        print('Situação: Aprovado')
    elif média >10:
        print('Situação: Ocorreu um erro pois você atribuiu em uma das notas um valor maior que 10')
    else:
        print('Situação: Reprovado')

    print('-----------------------------------------------------')

elif Lingua == 2:
        Nota_1 = int(input('Type your first mark here: '))
        Nota_2 = int(input('Type your second mark here: '))
        Nota_3 = int(input('Type your third mark here: '))
        Nota_4 = int(input('Type your fourth mark here: '))

        lista = [Nota_1, Nota_2, Nota_3, Nota_4]

        ## Cálculo da média:
        soma = (Nota_1 + Nota_2 + Nota_3 + Nota_4)
        média = (soma/4)

        ## Relatório
        print('-----------------------------------------------------')
        print('Results')
        print('')
        print('Mark addition result: ', soma)
        print ("Marks stored in the system: ", lista)
        print('')
        print('The meduim of all your mark is: ', média)

        ## Determinação da situação
        if média >= 7 and média <=10:
            print('Situation: Approved')
        elif média >10:
            print('Situation: An error occurred because you assigned a value greater than 10 to one of the grades.')
        else:
            print('Situação: Failed')
        print('-----------------------------------------------------')