#! python 3
'''
hangman.py juego de hangman, para practica de programacion.
'''
import random
import os


def imagen_hangman(oportunidad):
    lista_imagen = [
            '''
  +---+
  |   |
      |
      |
      |
      |
=========
            ''',
            '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
            ''',
            '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
            ''',
            '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
            ''',
            '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
            ''',
            '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
            ''',
            '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
            '''
            ]

    return lista_imagen[oportunidad]


def imagen_inicio():
    print('''

    _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/


    ''')


lista = ['carlos', 'luis']  # 'domingo', 'yelipsa']
tamano_lista = len(lista) - 1
palabra = random.choice(lista)
tamano_palabra = len(palabra)
lista_rayas = list('_' * tamano_palabra)

imagen_inicio()

contador_oportunidades = 0
contador_ganador = 0
game_over = False
while not game_over:
    print(' '.join(lista_rayas))
    letra = input('ingresa letra a descubrir: ')

    if letra in palabra:
        for index in range(tamano_palabra):
            if letra == palabra[index]:
                contador_ganador += 1
                lista_rayas[index] = letra
                os.system('cls')

        print(imagen_hangman(contador_oportunidades))
        if contador_ganador == tamano_palabra:
            print('you won!!!!')
            game_over = True

    else:
        # print(mostrar_en_rayas_esta_letra(palabra[index], index))
        contador_oportunidades += 1
        print(imagen_hangman(contador_oportunidades))
        print(f'esta letra {letra} no aparece en la lista, lo siento')        

        if contador_oportunidades > 5:
            print('you lose!!!!!!!!!!!')
            game_over = True
