lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    resp = input('Quer continuar? [S/N] ').upper()
    if resp != 'S':
        break
print('-' * 25)
print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('Não foi encontrado o valor 5 na lista.')

