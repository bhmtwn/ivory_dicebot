import json
import random
from add_char import add_char
from del_ch import dl_ch


def rand_fem(num_ch, user, name, id):
    n = -1
    try:
        with open(f'{id}_female.json', 'r') as file:
            characters = json.load(file)
    except IOError:
        print("Ошибка при чтении файла.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
    curr_len = len(characters)
    name = f"@id{user}({name})"
    random_clem = ""
    number = random.sample(range(1, curr_len), num_ch)
    while n+1 < num_ch:
        str_num = str(number[n])
        picked_character = characters[str_num]["name"]
        n = n + 1
        random_clem = random_clem + ", " + picked_character
    random_clem = name + "" + random_clem
    return(random_clem)

def rand_male(num_ch, user, name, id):
    n = -1
    try:
        with open(f'{id}_male.json', 'r') as file:
            characters = json.load(file)
    except IOError:
        print("Ошибка при чтении файла.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
    curr_len = len(characters)
    name = f"@id{user}({name})"
    random_clem = ""
    number = random.sample(range(1, curr_len), num_ch)
    while n+1 < num_ch:
        str_num = str(number[n])
        picked_character = characters[str_num]["name"]
        n = n + 1
        random_clem = random_clem + ", " + picked_character
    random_clem = name + "" + random_clem
    return(random_clem)

def rand_char(num_ch, user, name, id):
    n = -1
    name = f"@id{user}({name})"
    random_clem = ""
    try:
        with open(f'{id}.json', 'r') as file:
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
        random_clem = random_clem + ", " + picked_character
        n = n + 1
    random_clem = name + "" + random_clem
    return(random_clem)

def dice(num_of_sides, user, name, amount):
    name = f"@id{user}({name},)"
    result = ""
    res_list = []
    for i in range (amount):
        res_list = res_list + random.sample(range(1, num_of_sides+1), 1)
    result = (name + " " + str(res_list))
    return(result)

def add_ch(id, name_ch, sex, user, name):
    user = f"@id{user}({name},)"
    chat_id = id
    new_ch = {"name": name_ch, "sex": sex}
    line = add_char(new_ch, chat_id)
    response = (user + " персонаж добавлен в список")
    return(response)

def del_ch(id, name_ch, user, name):
        user = f"@id{user}({name},)"
        response = dl_ch(id, name_ch)
        text = (user + " " + response)
        return(text)