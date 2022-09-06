# Exercício 7
"""
dia = int(input('Qual o dia de hoje? '))
mes = int(input('Qual o mês da vez? '))
print(f'Já se passaram {(mes*30)+dia} dias')
print('-'*100)

# Exercicio 8

nota1 = float(input('Insira a primera nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
print(f'A média das notas inseridas é: {((nota1*1)+(nota2*2)+(nota3*3))/(1+2+3):.2f}')
print('-'*100)

# Exercicio 9

p = int(input('Insira a quantidade de camisas pequenas: '))*10
m = int(input('Insira a quantidade de camisas médias: '))*12
g = int(input('Insira a quantidade  de camisas grandes: '))*15

print(f'Total de valores de camisas em R$ \nP: R${p:.2f}\nM: R${m:.2f} \nG: R${g:.2f}'
      f'\nO total arrecadado é de R${p+m+g:.2f}')
print('-'*100)

# Exercício 11

DSA = int(input('Quantos dias estamos sem acidentes de trabalho? '))
anos = int(DSA / 365)
meses = int((DSA % 365) / 30)
dias = int((DSA % 365) % 30)
print(f'Estamos sem acidentas a {anos} anos, {meses} meses e {dias} dias')
print('-'*100)

# Exercício 12

sal = float(input('Qual o salário atual ? R$'))
nsal = sal+(sal*0.15)
print(f'O salário atual sem ajuste é de R${sal:.2f}'
      f'\nO salário com o aumento de 15% é de R${nsal:.2f}'
      f'\nO salário com descontos inclusos de 8% de impostos é R${nsal - (nsal * 8/100)}')
print('-'*100)

# Exercício 13

num = int(input('Insira um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
# Até 9999

print(f'===Resultado=== \nUnidades: {u} \nDezenas: {d} \nCentenas: {c} \nMilhares: {m}')
print('-'*50)
print('-'*100)

# Exercício 14

raio = float(input('Qual o comprimento do raio? '))
r = 3.14*raio**2
print(f'O comprimento dessa pizza é de : {r:.2f}CM')
print('-'*100)

# Exercicio 15 Triângulo retangulo

base = float(input('Insira o comprimento da base: '))
altura = float(input('Insira a altura: '))
print(f'O tamanho da área é: {(base*altura) / 2}M')
print('-'*100)

# Exercicio 16

gqueijo = float(2*0.050)
gpresunto = float(1*0.050)
ghamb = (1*0.100)
sanduba = int(input('Insira a quantidade de hambúrgueres a fazer: '))
print(f'Para {sanduba} sanduíches deve-se comprar:'
      f'\n{gqueijo*sanduba:.1f}KG de queijo'
      f'\n{gpresunto*sanduba:.1f}KG de presunto'
      f'\n{ghamb*sanduba:.1f}KG de carne')
print('-'*100)

# Exercicio 17

C = int(input('Quantos graus celsius? '))
F = (C*9/5) + 32
print(f'A resultado da conversão de {C} graus Celsius para {F} graus Farenheit')
print('-'*100)

# Exercicio 18

hrt = 10.00
hrtex = 15.00
hrtrabalhada = float(input('Quantas horas você trabalhou ?\n '))
horaextra = float(input('Quantas horas extras você fez ?\n'))
totalbruto = (hrtrabalhada*hrt)+(horaextra*hrtex)
print(f'Como você trabalhou {hrtrabalhada} horas.\n'
      f'Então seu salário bruto é R${totalbruto:.2f}\n'
      f'E o líquido é R${totalbruto - (totalbruto * 10/100):.2f}')
print('-'*100)

# Exercicio 19 alimento 2(3.50) ident 1(4)

furango = int(input("Insira a quantidade de frangos: "))
anelali = furango*(3.50*2)
ident = furango*4
print(f'Para {furango} frangos serão necessários:\n'
      f'{furango*2} Anéis de alimentação custando no total R${anelali:.2f}\n'
      f'{furango} Anéis de identificação custando no total R${ident:.2f}')
print('-'*75)
"""
# Exercicio 20
blusas = int(input(f'Quantas blusas foram produzidas ?\n'))
novelos = int(input('Quantos novelos foram usados ?\n'))
total = novelos / blusas
print(f'Foram necessários {total} novelos por blusa')
print('-'*100)
