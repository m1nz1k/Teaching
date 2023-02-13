import random                                       # либа рандома
def is_valid_random_number(num):                    # Проверка рандомного числа на правильность ввода
    if num.isdigit() == True and int(num) > 1:
        return True
    else:
        print('Введите пожалуйста целое число, которое больше 1')
        return False
def is_valid_user_number(num, total):               # Проверка числа пользователя
    if num.isdigit() == True:
        if int(num) < random_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            return False
        elif int(num) > random_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            return False
        elif int(num) == random_number:
            print('Вы угадали, поздравляем! Вы угадали с', total, 'раза !')
            return True
    else:
        return False
def is_valid_continuation(str):                     # repeat ?
    if str == 'n':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        return False
    elif str == 'y':
        print('Отлично !')
        return True
def start():                                        # Заголовок игры и выбор крайнего числа.
    print('Добро пожаловать в числовую угадайку')
    while (True):
        right = input('Введите крайнее правое число, до которого будет генерироваться рандомное число: ')
        if is_valid_random_number(right) == True:

            random_number = random.randint(1, int(right))
            return random_number
            break
        else:
            continue
def middle_game(total):                             # Пользователь угадывает число
    while (True):
        total += 1
        user_number = input('Вводи загаданное число число: ')
        if is_valid_user_number(user_number, total) == True:
            return user_number
            break
def next_game_or_not():                             # Повторяем игру или нет
    while (True):
        continuation = input('Еще разок сыграем? "y" да "n" нет. Твой выбор ? : ').lower()
        if is_valid_continuation(continuation) == True:
            return True
        else:
            return False

while(True):                         # Исполнение игры
    total = 0
    left = 1
    random_number = start()
    user_number = middle_game(total)
    if next_game_or_not() == True:
        continue
    else:
        break



