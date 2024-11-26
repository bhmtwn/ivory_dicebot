import json

def dl_ch(id, name_ch):
    check = 0
    new_list = {}
    new_m_list = {}
    new_f_list = {}
    try:
        with open(f'{id}.json', 'r') as file:
            characters = json.load(file)
    except IOError:
        print("Ошибка при чтении файла.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
    
    try:
        with open(f'{id}_female.json', 'r') as file:
            female = json.load(file)
    except IOError:
        print("Ошибка при чтении файла.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")
       
    try:
        with open(f'{id}_male.json', 'r') as file:
            male = json.load(file)
    except IOError:
        print("Ошибка при чтении файла.")
    except json.JSONDecodeError:
        print("Ошибка при декодировании JSON.")   
            
    for i in range (len(characters) - 1):
        i = i + 1
        str_i = str(i)
        if characters[str_i]["name"] == name_ch:
            print(characters[str_i])
            check_sex = characters[str_i]["sex"]
            print(check_sex)
            del characters[str_i]
            check = 1
            if check_sex == "f":
                new_m_list = male
                check_f = 0
                for v in range(len(female) - 1):
                    v = v + 1
                    str_v = str(v)
                    if female[str_v]["name"] == name_ch:
                        print(female[str_v])
                        del female[str_v]
                        check_f = 1
                        continue
                    if check_f == 0:
                        new_f_list[str_v] = female[str_v]
                    elif check_f == 1:
                        new_f_list[str(v - 1)] = female[str_v]    
            elif check_sex == "m":
                new_f_list = female
                check_m = 0
                for c in range(len(male) - 1):
                    c = c + 1
                    str_c = str(c)
                    if male[str_c]["name"] == name_ch:
                        del male[str_c]
                        check_m = 1
                        continue
                    if check_m == 0:
                        new_m_list[str_c] = male[str_c]
                    elif check_m == 1:
                        new_m_list[str(c - 1)] = male[str_c]
            continue
        if check == 0:
            new_list[str_i] = characters[str_i]
        elif check == 1:
            new_list[str(i - 1)] = characters[str_i]

    if check == 0:
        response = "такого персонажа нет"
        return(response)
    
    else:
        try:
            with open(f'{id}.json', 'w') as file:
                json.dump(new_list, file, indent=4)
            print("Данные успешно записаны в файл.")
        except IOError:
            print("Ошибка при записи в файл.")
        except json.JSONEncodeError:
            print("Ошибка при кодировании JSON.")

        try:
            with open(f'{id}_female.json', 'w') as file:
                json.dump(new_f_list, file, indent=4)
            print("Данные успешно записаны в файл.")
        except IOError:
            print("Ошибка при записи в файл.")
        except json.JSONEncodeError:
            print("Ошибка при кодировании JSON.")

        try:
            with open(f'{id}_male.json', 'w') as file:
                json.dump(new_m_list, file, indent=4)
            print("Данные успешно записаны в файл.")
        except IOError:
            print("Ошибка при записи в файл.")
        except json.JSONEncodeError:
            print("Ошибка при кодировании JSON.") 

        response = "персонаж удален"
        return(response)   
