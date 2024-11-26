import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType 
from config import token
from functions import rand_char, rand_fem, rand_male, dice, add_ch, del_ch

print ('до сессии')

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 165216405)

#165216405_айвори 191026018_хаус

print ('до сендера')

def sender(id, text):
    vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})

print ('до лонгпула')

for event in longpoll.listen(): 
    if event.type == VkBotEventType.MESSAGE_NEW:

        #первичный обработчик сообщений: выделяет текст до пробела и передаёт его дальше
        msg = event.object.message['text']
        test_msg = msg.split(' ', 1)
        call = str(test_msg[0])

        if event.from_chat:
            #получаем данные пользователя, отправившего сообщение
            user = event.object.message['from_id']
            user_get=vk.users.get(user_ids = (user))
            user_get=user_get[0]
            name=user_get['first_name']
            id = event.chat_id 
            match call[0:3]:
                case '/ch' | '/рп':
                    len_msg = len(call)
                    print(len_msg)
                    if len_msg > 2:
                        num_cmd = call[3:]
                    else:
                        num_cmd = 1
                    try:
                        num_ch = int(num_cmd)
                    except:
                        num_ch = 1
                    text_msg = rand_char(num_ch, user, name, id)
                    sender(id, text_msg)
                case '/rf' | '/рд':
                    len_msg = len(call)
                    if len_msg > 2:
                        num_cmd = call[3:]
                    else:
                        num_cmd = 1
                    try:
                        num_ch = int(num_cmd)
                    except:
                        num_ch = 1
                    text_msg = rand_fem(num_ch, user, name, id)
                    sender(id, text_msg)
                case '/rm' | '/рм':
                    len_msg = len(call)
                    if len_msg > 2:
                        num_cmd = call[3:]
                    else:
                        num_cmd = 1
                    try:
                        num_ch = int(num_cmd)
                    except:
                        num_ch = 1
                    text_msg = rand_male(num_ch, user, name, id)
                    sender(id, text_msg)
                case '/dc' | '/кб':
                    new_line = call.split('.', 1)
                    len_msg = int(len(new_line[0]))
                    num_dice = new_line[0]
                    num_cmd = num_dice[3:]
                    if len_msg > 1:
                        try:
                            num_of_sides = int(num_cmd)
                        except:
                            num_of_sides = 20
                        try:
                            amount = int(new_line[1])
                        except:
                            amount = 1
                    else: 
                        num_of_sides = 20
                        amount = 1
                    text_msg = dice(num_of_sides, user, name, amount)
                    sender(id, text_msg)
                case '/ad':
                    add_msg = msg.split()
                    name_ch = add_msg[1]
                    sex = add_msg[2]
                    text_msg = add_ch(id, name_ch, sex, user, name)
                    sender(id, text_msg)
                case '/dl':
                    del_msg = msg.split()
                    name_ch = del_msg[1]
                    text_msg = del_ch(id, name_ch, user, name)
                    sender(id, text_msg)

print ('done')


