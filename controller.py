# -*- coding: windows-1251 -*-
import pandas as pd

import get_comments_from_vk
import remap_data
import vk_messages_bot

TOKEN = "123abc"  # ����� - �������� ����
# ��� �����, � ������� ����� ����������� excel
DATASET_NAME = "category_dataset.csv"
# id ������ �� ������� ����� ����
# id ������ ������ ���������� � -
groupID = "-96717639"
# id ������ � ������� �� ����������� ����
long_poll_group_id = "-012345"


def start_service():
    # �����������������
    # �������� ����� � ������ �� ���� ��� �������������� � ������� � �������� �������
    auth = get_comments_from_vk.auth()

    # �������� ����������� � ��������� �� � commentary_dataset.csv
    data = get_comments_from_vk.getDataFromComments(auth, groupID)

    # ����� �� ������������ � ������� ���������� -> ����� �� ������������
    data = remap_data.clean_data(data)

    # ����� �� ������������ -> �����������
    data = remap_data.get_category_dataset(data)

    # ��������� ������
    data.to_csv(DATASET_NAME, encoding="windows-1251")

    vk_messages_bot.start_bot(data, token=TOKEN, long_poll_group_id=long_poll_group_id)
    print(data)


def start_vk_bot():
    data = pd.read_csv(DATASET_NAME, encoding="windows-1251", index_col=0)
    vk_messages_bot.start_bot(data, token=TOKEN, long_poll_group_id=long_poll_group_id)


start_service()
