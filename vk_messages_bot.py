# -*- coding: windows-1251 -*-

from random import randint

import vk_api
from requests import *

from get_stops_from_data import get_stops_by_time


def start_bot(data, token):
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    print("bot started")
    longPoll = vk.groups.getLongPollServer(group_id=183524419)
    server, key, ts = longPoll['server'], longPoll['key'], longPoll['ts']
    while True:
        # Последующие запросы: меняется только ts
        longPoll = post('%s' % server, data={'act': 'a_check',
                                             'key': key,
                                             'ts': ts,
                                             'wait': 25}).json()
        if longPoll['updates'] and len(longPoll['updates']) != 0:
            for update in longPoll['updates']:
                if update['type'] == 'message_new':
                    # Помечаем сообщение от этого пользователя как прочитанное
                    vk.messages.markAsRead(peer_id=update['object']['user_id'])
                    user = update['object']["user_id"]
                    text = get_stops_by_time(data)

                    if text is None or text == {}:
                        message = "нет записей"
                        vk.messages.send(user_id=user, random_id=randint(-2147483648, 2147483647),
                                         message=message)
                        print(message)
                        ts = longPoll['ts']
                        continue

                    message = "чем больше вероятность - тем больше шанс встретить контролёра\n" \
                              "\nостановка вероятность\n"
                    for i in text.items():
                        message += i[0] + "  "
                        message += str(i[1])
                        message += "\n"

                    vk.messages.send(user_id=user, random_id=randint(-2147483648, 2147483647),
                                     message=message)
                    ts = longPoll['ts']
