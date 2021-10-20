
import os
clear = lambda: os.system('clear')
clear()

def diag(n):
    if n > 3:
        print(f'O poligono de {n} lados possui {int((n**2 - 3* n )/2)} diagonais.')
    else:
        print('Poligono Inválido, ou 0 diagonais.')
def lados(d):
    if d > 0:
        delta = (d * 8 + 9)**0.5
        resp_cert = float((3 + delta) / 2)
        if resp_cert.is_integer() == False or resp_cert < 2:
            resp_cert = 0
        if resp_cert != 0:
            print(f'O polígono com {d} diagonais é o que possui {int(resp_cert)} lados! ')
        else:
            print(f'Não existe um poligono com {d} diagonais.')
def continuar():
    while True:
        cont = str(input('Quer continuar?[s/n]  ')).upper().strip()[0]
        if cont not in 'SN':
            print('Erro. Valor inválido, Tente novamnete.')
        else:
            return cont


cont = ''
while cont != 'N':
    while True:
        print('=-'* 50)
        fazer = int(input('''O que você quer fazer? 
   [ 1 ] Descobrir a quantidade de diagonais de um poligono(sabendo a quantidade de lados).  
   [ 2 ] Descobrir a quantidades de lados de um poligono(sabendo a quantidade de diagonais).
   [ 3 ] Sair.
   Resposta:  '''))
        print('=-'* 50)
        if fazer == 1:
            diag(int(input('Quantos lados tem o poligono?  ')))
            break
        elif fazer == 2:
            lados(int(input('Quantas diagonais tem o poligono?  ')))
            break
        elif fazer == 3:
            break
        else:
            print('Erro! Opção inválida.')
    if fazer == 3:
        break
    cont = continuar()
    clear()
clear()