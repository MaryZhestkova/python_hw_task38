from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
                    f"1 вариант: \n "
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 вариант: \name"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print('Неправильный ввод!')
        var = int(input('Введите число 1 или 2'))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")   
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")   

def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_list = []
            j = 0
            for i in range(len(data_first)):
                 if data_first[i] == '\n' or i == len(data_first) - 1:
                      data_first_list.append(''.join(data_first[j:i+1]))
                      j = i
            print(''.join(data_first_list))
    print("Вывожу данные из 2 файла: \n")
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
         data_second = f.readlines()
         for line in data_second:
              print(line.strip())

def edit_data():
    choice = int(input("В какаом файле нужно внести изменения:\n1 - Изменить данные в 1 файле\n2 - Изменить данные во 2 файле\n"))
    while choice != 1 and choice != 2:
        print("Неправильный ввод")
        choice = int(input("Выберите вариант:\n1 - Изменить данные в 1 файле\n2 - Изменить данные во 2 файле\n"))

    if choice == 1:
        with open("data_first_variant.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()        

        print("Доступные для изменения данные:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите изменить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки, которую хотите изменить: "))

        new_data = input("Введите новые данные: ") 

        data[line_number-1] = new_data + " \n"

        with open("data_first_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Спасибо, изменения сохранены")

    elif choice == 2:
        with open("data_second_variant.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()            

        print("Доступные для изменения данные:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите изменить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки, которую хотите изменить: "))

        new_data = name_data() + "; " + surname_data() + "; " + phone_data() + "; " + address_data()

        data[line_number-1] = new_data + "\n"

        with open("data_second_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Спасибо, изменения сохранены")


def delete_data():
    variant = int(input("Выберите вариант:\n1 - Удалить данные из первого файла\n2 - Удалить данные из второго файла\n"))
    while variant != 1 and variant != 2:
        print("Неправильный ввод")
        variant = int(input("Выберите вариант:\n1 - Удалить данные из первого файла\n2 - Удалить данные из второго файла\n"))

    if variant == 1:
        with open("data_first_variant.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()

        print("Доступные для удаления данные:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите удалить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки, которую хотите удалить: "))

        del data[line_number-1]

        with open("data_first_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Спасибо, данные удалены")

    elif variant == 2:
        with open("data_second_variant.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()

        print("Доступные для удаления данные:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите удалить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки, которую хотите удалить: "))

        del data[line_number-1]

        with open("data_second_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Спасибо, данные удалены")