# Учись считать

import random

lowDigit = 50       # Нижний порог
highDigit = 100     # Верхний порог    

symbol = 0          # Знак в пимере +, -, *, /

count= 0      # Сколько ходов было
playGame = True     # Главный цикл игры
score = 0           # Очки пользователя
right = 0

x = 0               # 1 Число в примере
y = 0               # 2 Число в примере
z = 0               # Результат примера
# =================================================

print("""Приветсвуем в нашей игре на удачу! Поиграйте с компьютером.
Для выхода из игры, наберите - STOP. Для продолжения - 1.
Удачи!""")
print('-' * 10)

# ГЛАВНЫЙ
while (playGame):
    count = 0
    score = startScore
    print(f'Ваши очки: {score}')
    print(f'')
    print(f'')
    print(f'')
    
    symbol = random.randint(0, 3)
    # 0 - плюс
    # 1 - минус
    # 2 - умножить
    # 3 - делить

    # --------------------- Сложение
    if (symbol == 0):
        z = random.randint(lowDigit, highDigit)
        x = random.randint(lowDigit, z)
        y = z - x
        if (random.randint(0, 1) == 0):
            print(f'{x} + {y} = ?')
        else:
            print(f'{y} + {x} = ?')
    # --------------------- Вычитание
    elif (symbol == 1):
        x = random.randint(lowDigit, highDigit)
        y = random.randint(0, x - lowDigit)
        z = x - y
        print(f'{x} - {y} = ?')
    # --------------------- Умножение
    elif (symbol == 2):
        x = random.randint(1, highDigit - lowDigit) // 2 + 1
        y = random.randint(lowDigit, highDigit) // x + 1
        z = x * y
        print(f'{x} * {y} = ?')
    # --------------------- Деление
    elif (symbol == 3):
        x = random.randint(1, (highDigit - lowDigit)) // 10 + 1
        y = random.randint(lowDigit, highDigit) // x
        if (y == 0):
            y = 1
        x = x * y
        z = x // y
        print(f'{x} / {y} = ?')



# -------- помощь пользавателю и конец игры
    user = ''
    while (not user.isdigit()
           and user.upper() != 'STOP'
           and user.upper() != 'S'
           and user.upper() != 'Ы'
           and user.upper() != 'ЫЕЩЗ'):
        user = input('Ваш ответ: ')
    if (not user.isdigit()):
        print('-' * 27)

        if (user.upper() == 'HELP'
                or user == '?'
                or user == ','
                or user.upper() == 'РУДЗ'):
            if (z > 9):
                print('Последняя цифра ответа: {z % 10}')
            else:
                print('Ответ состоит из одной цифры, подсказка невозможна.')
            score -= 10
# ----------------------------------------------------
        elif (user.upper() == 'STOP'
              or user.upper() == 'S'
              or user.upper() == 'Ы'
              or user.upper() == 'ЫЕЩЗ'):
            playGame = False
        else:
            count += 1
            
            if (int(user) == z):
                print('\nПравильно!\n')
                right += 1
                score += 10
            else:
                print(f'\nОтвет неправильный... Правильно: {z}')
                print(f'Вы можете ввести команду HELP или ? Чтобы увидеть последнюю цифру ответа (-10 очков)\n')
                score -= 20
       



print('-' * 25)
print('СТАТИСТИКА ИГРЫ:')
print(f'Всего примеров: {count}')
print(f'Правильных ответов: {right}')
print(f'Неправильных ответов: {count - right}')
if (count > 0):
    print(f'Процент верных ответов: {int(right / count * 100)}%')
else:
    print(f'Процент верных ответов: 0%')
print("""Спасибо за игру, было весело. Ждём вам снова.
Дальше примеры будут только интереснее ^~~~^""")
# КОНЕЦ
