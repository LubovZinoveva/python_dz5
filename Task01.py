''' Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом"" '''

import random

def move_frend(n, limit = 28):
    take_sweets = int(input('Сколько заберете конфет: '))
    if int(n) < limit:
        limit = n
    if take_sweets > limit:
        print(f'Ошибка, можно взять не больше {limit}')
        move_frend(n)
    elif take_sweets < 1:
        print(f'Ошибка, возьмите от 1 до {limit} конфет')
        move_frend(n)
    else:
        n -= take_sweets
        print(f'Осталось {n} конфет(ы)')
        return n

def move_bot(number_sweets):
    if number_sweets < 29:
        take = number_sweets
    elif 29 < number_sweets < 57:
        take = number_sweets - 29
    else:
        take = random.randint(1, 28)
    number_sweets -= take
    print(f'Бот забрал {take} конфет(ы)')
    print(f'Осталось {number_sweets} конфет(ы)')
    return number_sweets

def play_with_bot(count, player):
    step = 1
    print(f'На столе лежит {count} конфет')
    if move1 == 1:
        print(f'{player}, вы ходите первым(ой)')
        while count > 0:
            print()
            print(f'Ход {step}')
            count = move_frend(count)
            if count == 0:
                print(f'Поздравляем, {player}, вы выиграли!')
                break
            count = move_bot(count)
            if count == 0:
                print('Бот выиграл')
            step += 1
    else:
        print('Бот ходит первым')
        while count > 0:
            print()
            print(f'Ход {step}')
            count = move_bot(count)
            if count == 0:
                print('Бот выиграл')
                break
            count = move_frend(count)
            if count == 0:
                print(f'Поздравляем, {player}, вы выиграли!')
            step += 1

def play_with_frend(count, player1, player2):
    step = 1
    print(f'На столе лежит {count} конфет')
    if move1 == 1:
        print(f'{player1} ходит первым(ой)')
        while count > 0:
            print()
            print(f'Ход {step}')
            print(f'{player1} ходит')
            count = move_frend(count)
            if count == 0:
                print(f'{player1} выиграл(а). Поздравляем!')
                break
            print(f'{player2} ходит')
            count = move_frend(count)
            if count == 0:
                print(f'{player2} выиграл(а). Поздравляем!')
            step += 1
    else:
        print(f'{player2} ходит первым(ой)')
        while count > 0:
            print()
            print(f'Ход {step}')
            print(f'{player2} ходит')
            count = move_frend(count)
            if count == 0:
                print(f'{player2} выиграл(а). Поздравляем!')
                break
            print(f'{player1} ходит')
            count = move_frend(count)
            if count == 0:
                print(f'{player1} выиграл(а). Поздравляем!')
            step += 1

try:
    sweets = 105
    move1 = random.randint(1, 2)
    print('2 режима игры: 1. С другом 2. С ботом')
    variant = int(input('Выберите режим игры: '))
    if variant == 1:
        name1 = input("Введите имя первого игрока: ")
        name2 = input("Введите имя второго игрок: ")
        play_with_frend(sweets, name1, name2)
    elif variant == 2:
        name = input("Введите имя игрока: ")
        play_with_bot(sweets, name)
    else:
        print('Ошибка, выберите 1 или 2')
except:
    print('Ошибка, введите число')

