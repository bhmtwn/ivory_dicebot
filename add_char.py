import json
import random

def add_char(new_char, id):
    try:
        with open(f'{id}.json', 'r') as file:
            characters_list = json.load(file)
        print("Данные успешно записаны в файл.")
    except IOError:
        print("Ошибка при записи в файл.")
    except json.JSONEncodeError:
        print("Ошибка при кодировании JSON.")

    try:
        with open(f'{id}_female.json', 'r') as file:
                characters_f_list = json.load(file)
    except IOError:
            print("Ошибка при чтении файла.")
    except json.JSONDecodeError:
            print("Ошибка при декодировании JSON.")

    try:
        with open(f'{id}_male.json', 'r') as file:
            characters_m_list = json.load(file)
        print("Данные успешно записаны в файл.")
    except IOError:
        print("Ошибка при записи в файл.")
    except json.JSONEncodeError:
        print("Ошибка при кодировании JSON.")

    next_item = len(characters_list)
    next_f_item = len(characters_f_list)
    next_m_item = len(characters_m_list)

    characters_list[next_item] = new_char
    if new_char['sex'] == 'm':
        characters_m_list[next_m_item] = new_char
    elif new_char['sex'] == 'f':
        characters_f_list[next_f_item] = new_char

    characters_f_list[next_f_item] = new_char

    try:
        with open(f'{id}.json', 'w') as file:
            json.dump(characters_list, file, indent=4)
        print("Данные успешно записаны в файл.")
    except IOError:
        print("Ошибка при записи в файл.")
    except json.JSONEncodeError:
        print("Ошибка при кодировании JSON.")

    try:
        with open(f'{id}_female.json', 'w') as file:
            json.dump(characters_f_list, file, indent=4)
        print("Данные успешно записаны в файл.")
    except IOError:
        print("Ошибка при записи в файл.")
    except json.JSONEncodeError:
        print("Ошибка при кодировании JSON.")

    try:
        with open(f'{id}_male.json', 'w') as file:
            json.dump(characters_m_list, file, indent=4)
        print("Данные успешно записаны в файл.")
    except IOError:
        print("Ошибка при записи в файл.")
    except json.JSONEncodeError:
        print("Ошибка при кодировании JSON.")

    return('done')
