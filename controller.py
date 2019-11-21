# -*- coding: windows-1251 -*-
import pandas as pd

import get_comments_from_vk
import remap_data
import vk_messages_bot

TOKEN = "123abc"  # токен - вставьте свой
DATASET_NAME = "dataset_v2_corrected.csv"


def start_service():
    # аутентифицируемся
    # замените логин и пароль на свой для аутентификации и доступа к закрытым группам
    auth = get_comments_from_vk.auth()

    # получаем комментарии и созраняем их в commentary_dataset.csv
    data = get_comments_from_vk.getDataFromComments(auth)

    # стоят на университете в сторону универмага -> стоят на университете
    data = remap_data.clean_data(data)

    # стоят на университете -> университет
    data = remap_data.get_category_dataset(data)

    # сохраняем данные
    data.to_csv("category_dataset.csv", encoding="windows-1251")

    vk_messages_bot.start_bot(data, token=TOKEN)
    print(data)


def start_vk_bot():
    data = pd.read_csv(DATASET_NAME, encoding="windows-1251", index_col=0)
    vk_messages_bot.start_bot(data, token=TOKEN)


start_service()
