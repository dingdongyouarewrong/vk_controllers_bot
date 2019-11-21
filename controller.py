# -*- coding: windows-1251 -*-
import pandas as pd

import get_comments_from_vk
import remap_data
import vk_messages_bot

TOKEN = "123abc"  # ����� - �������� ����
DATASET_NAME = "dataset_v2_corrected.csv"


def start_service():
    # �����������������
    # �������� ����� � ������ �� ���� ��� �������������� � ������� � �������� �������
    auth = get_comments_from_vk.auth()

    # �������� ����������� � ��������� �� � commentary_dataset.csv
    data = get_comments_from_vk.getDataFromComments(auth)

    # ����� �� ������������ � ������� ���������� -> ����� �� ������������
    data = remap_data.clean_data(data)

    # ����� �� ������������ -> �����������
    data = remap_data.get_category_dataset(data)

    # ��������� ������
    data.to_csv("category_dataset.csv", encoding="windows-1251")

    vk_messages_bot.start_bot(data, token=TOKEN)
    print(data)


def start_vk_bot():
    data = pd.read_csv(DATASET_NAME, encoding="windows-1251", index_col=0)
    vk_messages_bot.start_bot(data, token=TOKEN)


start_service()
