from logger import *


def interface():
    print('Добрый день! Это бот-помощник. \n'
          'Что вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные \n'
          '3 - Изменить данные \n'
          '4 - Удалить данные')
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 5:
        command = int(input('Ошибка! Ваш выбор: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_data() 
    elif command == 4: 
        delete_data()
              



interface()
