bordas = '\033[037m-=-\033[m' * 12
print(bordas)
print('{:^35}'.format('REAJUSTE DE SALÁRIO'))
print(bordas)
print()

s = ''

while type(s) != float:
    try:
        s = float(input('Digite o salário do funcionário: R$ '))
    except:
        print('Por favor digite um salário válido!')

a = ''

while type(a) != float:
    try:
        a = float(input('Digite a porcentagem de aumento: '))
    except:
        print('Por favor digite uma porcentagem válida!')

print(f'Com o aumento de {a}% o valor do aumento será de R${s*(a/100):.2f} e o funcionário que ganhava R${s:.2f} vai '
      f'passar a ganhar R${s+s*(a/100):.2f}.')
