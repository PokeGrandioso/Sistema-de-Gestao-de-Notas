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