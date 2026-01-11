import json
import random
from add_char import add_char
from del_ch import dl_ch


def rand_fem(num_ch):
    n = -1
    try:
        with open('1_female.json', 'r') as file:
            characters = json.load(file)
    except IOError:
        print("Ошибка при чтении файла.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
    curr_len = len(characters)
    random_clem = ""
    number = random.sample(range(1, curr_len+1), num_ch)
    while n+1 < num_ch:
        str_num = str(number[n])
        picked_character = characters[str_num]["name"]
        if n+2 == num_ch:
            random_clem = random_clem + picked_character
            n = n + 1
            continue
        else:
            n = n + 1
            random_clem = picked_character + ", " + random_clem
    return(random_clem)

def rand_sticker():
    n = -1
    try:
        with open(f'stickers.json', 'r') as file:
            stickers = json.load(file)
    except IOError:
        print("Ошибка при чтении файла.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
    curr_len = len(stickers)
    number = random.sample(range(1, curr_len+1), 1)
    str_num = str(number[n])
    picked_sticker = stickers[str_num]["id"]
    return(picked_sticker)

def rand_male(num_ch):
    n = -1
    try:
        with open('1_male.json', 'r') as file:
            characters = json.load(file)
    except IOError:
        print("Ошибка при чтении файла.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
    curr_len = len(characters)
    random_clem = ""
    number = random.sample(range(1, curr_len), num_ch)
    while n+1 < num_ch:
        str_num = str(number[n])
        picked_character = characters[str_num]["name"]
        if n+2 == num_ch:
            random_clem = random_clem + picked_character
            n = n + 1
            continue
        else:
            n = n + 1
            random_clem = picked_character + ", " + random_clem
    return(random_clem)

def rand_ch(num_ch):
    n = -1
    random_clem = ""
    try:
        with open('1.json', 'r') as file:
            characters = json.load(file)
    except IOError:
        print("Ошибка при чтении файла.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
    curr_len = len(characters)
    number = random.sample(range(1, curr_len), num_ch)
    while n+1 < num_ch:
        str_num = str(number[n])
        picked_character = characters[str_num]["name"]
        if n+2 == num_ch:
            random_clem = random_clem + picked_character
            n = n + 1
            continue
        else:
            n = n + 1
            random_clem = picked_character + ", " + random_clem
    return(random_clem)

def dice(num_of_sides, amount):
    result = ""
    res_list = []
    for i in range (amount):
        res_list = res_list + random.sample(range(1, num_of_sides+1), 1)
    result = (str(res_list))
    return(result)

def add_ch(name_ch, sex):
    new_ch = {"name": name_ch, "sex": sex}
    line = add_char(new_ch)
    response = ("Персонаж добавлен в список")
    return(response)

def del_ch(name_ch):
        response = dl_ch(name_ch)
        return(response)

def player():
    n = -1
    random_clem = ""
    try:
        with open('players.json', 'r') as file:
            players = json.load(file)
    except IOError:
        print("Ошибка при чтении файла.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
    curr_len = len(players)
    number = str(random.randint(1, curr_len))
    picked_character = players[number]["name"]
    return(picked_character)