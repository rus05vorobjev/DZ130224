from data_create import input_user_data



def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))


def change_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        list_1 = file.readlines()
        list_1 = [i.strip("\n") for i in list_1 if i != '\n']
        list_1 = [list(list_1[i:i+4]) for i in range(0, len(list_1), 4)]
        num = 1
        for line in list_1:
            print(f"{num} абонент -{line}")
            num += 1    
        print('')
        index_delete = int(input("Введите номер абонента: ")) 
        print(list_1[index_delete - 1])
        qwestion_1 = input('Какой элемент изменить?\n1 - name\n2 - surname\n3 - phone\n4 - adress\nВыбор:  ')
        if qwestion_1 == "1":
            list_1[index_delete - 1][0] = input('На что меняем?\n: ')
        elif qwestion_1 == "2":
            list_1[index_delete - 1][1] = input('На что меняем?\n: ')
        elif qwestion_1 == "3":
            list_1[index_delete - 1][2] = input('На что меняем?\n: ')
        elif qwestion_1 == "4":
            list_1[index_delete - 1][3] = input('На что меняем?\n: ') 

    
    print(list_1)       

        
    with open ('data_first_variant.csv', 'w', encoding='utf-8') as file:
        for line in list_1:
            print('')
            for i in line:
                file.write(f'{i}\n')

        print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        list_1 = file.readlines()
        list_1 = [i.strip("\n") for i in list_1 if i != '\n']
        list_2 = []
        num = 1
        for i in list_1:
           
           line = i.split(";")
           
           
           print(f"{num} абонент -{line}")
           num += 1
           list_2.append(line)    
        print('')
        
        index_delete = int(input("Введите номер абонента: ")) 
        print(list_2[index_delete - 1])
        qwestion_1 = input('Какой элемент изменить?\n1 - name\n2 - surname\n3 - phone\n4 - adress\nВыбор:  ')
        if qwestion_1 == "1":
            list_2[index_delete - 1][0] = input('На что меняем?\n: ')
        elif qwestion_1 == "2":
            list_2[index_delete - 1][1] = input('На что меняем?\n: ')
        elif qwestion_1 == "3":
            list_2[index_delete - 1][2] = input('На что меняем?\n: ')
        elif qwestion_1 == "4":
            list_2[index_delete - 1][3] = input('На что меняем?\n: ')

        
    
    print(list_2)
    
    
    with open ('data_second_variant.csv', 'w', encoding='utf-8') as file:
        for i in list_2:
            file.write(f'{";".join(i)}\n')

def delete_data():

 
    print('1 файл:')

    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        list_1 = file.readlines()
        list_1 = [i.strip("\n") for i in list_1 if i != '\n']
        
        list_1 = [list(list_1[i:i+4]) for i in range(0, len(list_1), 4)]
        num = 1
        for line in list_1:
            print(f"{num} абонент -{line}")
            num += 1    
        
        index_delete = int(input("Введите номер абонента для удаления: ")) 
        print(list_1[index_delete - 1])
        print('')
        qwestion_1 = input('Удалить абонента? y/n\n Выбор: ')
        if qwestion_1 == "y":          
            deleted = list_1[index_delete - 1]
            del list_1[index_delete - 1]
            print(f"Удалена запись: {deleted}\n")
        elif qwestion_1 == "n":   
            index_delete = int(input("Введите номер абонента для удаления: "))
        else:
            index_delete = int(input("Ошибка! Введите номер абонента для удаления: "))

                        
        list_1 = sum(list_1, [])
        print(list_1)    
        
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write("\n".join(list_1))
            print(list_1)        
                  

        
    print('2 файл:')
        
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        list_1 = file.readlines()
        list_1 = [i for i in list_1 if i != '\n']
        list_1 = list_1[:]
        
        num = 1
        for line in list_1:
            print(f"{num} абонент -{line}")
            num += 1    
        print('Для выхода введите "q"')
        index_delete = int(input("Введите номер абонента для удаления: ")) 
        print(list_1[index_delete - 1])
        print('')
        qwestion_1 = input('Удалить абонента? y/n\n Выбор: ')
        if qwestion_1 == "y":          
            deleted = list_1[index_delete - 1]
            del list_1[index_delete - 1]
            print(f"Удалена запись: {deleted}\n")
        elif qwestion_1 == "n":   
            index_delete = int(input("Введите номер абонента для удаления: "))
        else:
            index_delete = int(input("Ошибка! Введите номер абонента для удаления: "))
                 
            
    with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
        file.write("\n".join(list_1))
        print(list_1)
        

        
        
         

    

          


          



