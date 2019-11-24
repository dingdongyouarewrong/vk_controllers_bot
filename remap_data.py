# -*- coding: windows-1251 -*-

import numpy as np

stops = ['���������', '�������', '�������������', '�������������', '�����������', '���������',
         '�����������', '����������', '8 �����',
         '�������� ��� ��������', '�������� ��������', '����', '���������', '������c���',
         '��������', '���', '�������', '�����������', '������', '1000 �������', '�������', '������',
         '���� �����������', '��������������������', '���������', '��� 18', '��������', '���������',
         '�����������������', '��������', '����� ���������', '����� �����������', '���������',
         '���� ���', '����������',
         '�������', '��� �1', '�� ��������', '����������', '������������ ��������', '������ �����',
         '��������', '����������', ' �������������', '������������', '���������������', '������',
         '����������', '������', '��������������', '������������������', '2�� �����', '��������',
         '��������� �����', '���������', '������ �����', '����', '�����������', '��������',
         '����67', '35�', '��������', '50 ��� ������ ����������', '�����', '����������',
         '���������', '�����������', '����������', ' �������� ����������', '�����������',
         '���� ���������', '���������', '�������� ���', '�� ����������', '�������', ' ��������',
         '�������', '������', '������', '������������', '�������������', '����������', '�������',
         '���������', '������������������', '���������', '��������', '���', '���', '������',
         '����������� ���', '��������', '�������', '����������', '���������', '��������',
         '��������', '����������� �����', '������ ������������', '9 ���', ' ������', '���������',
         '������� �����', '���������', '�������������', '���������', '��������� ������', '������',
         '��������', '���������', '�����������', '������', '�������������', '�������',
         '������������������', '������', '60 ���', '���������', '���������',
         '�������������� ���������', '���������� ���', '���������', '������', '�����', '��������',
         '��������', '�����������', '������', '�����������', '���������', '������ ������ ��������',
         '�����������', '���������', '��������', '���������', '���������', '���������������', '���',
         '����������', '������� ��� 11', '���������', '�����', '�����������', '�����', '��������',
         '����������', '������', '���', '���������', '�����������������', '������',
         '70 ���', '�������������', '�������� �����', '��������', '���������', '������������',
         '��������', '������', '����', '�������', '2� �������� �������', '�������', '������',
         '�������������� ���������', '�������', '������', '1�� �����', '������� �����',
         '���������������', '���������', '���������', '���������', '��������', '���', '����',
         '���������', '������� �����', '�����', '���', '����������', '�����', '������', '���������',
         '����������', '������', '�������', '������������ �����������', '������������',
         '������������', '����������', '����������', '�������', '����������',
         '���������� ���������', '�����������', '��������������', '�������������', '�������������',
         '�������', '������ ������', '�������', '������ ��������', '�����������', '�������',
         '�������', '���������', '���������������� ��������', '�������������������', '����',
         '������� ����������', '�� 6', '�����������', '������������ ����', '��������� ������',
         '����� �����', '������', '������� �����', '3�� �����', '������', '������� ����',
         '���������', '�����������', '���������', '������� ����', '���������', '������� ���������',
         '���������', '����������', '��� 21', '�����', '������������������', '��������',
         '���������', '�����������������', '��� 20�', '��� ��������', ' ����������', '��������',
         '������� �������������� ���������', '�������', '�� ������������', '�������� �����',
         '������������', '������������', '����� ���� 27', '�������������', '������', '�����������',
         '���179', '����������', '�������� �����', '���������', '���������� ����',
         '�������� ��������', '������', '����������', '��������', '���������������', '��� 19']
# import pymorphy2
from fuzzywuzzy import process


def clear_commentary(text):
    """������� ������ ����� ����������� -
   ����������� �� ������� ����� ���������"""
    index = 0
    splitted = text.split(" ")
    for i, s in enumerate(splitted):
        if len(splitted) == 1:
            return np.NaN
        if ((("������" in s) or ("�����" in s) or (
                "���" in s) or (
                     "����" in s)) and s is not ""):
            index = i
    if index is not 0 and index < len(splitted) - 2:
        for i in range(1, 4):
            splitted.remove(splitted[index])
        string = " ".join(splitted)
        text = (string.lower())
    elif index is not 0:
        splitted = splitted[:index]
        string = " ".join(splitted)
        text = string.lower()
    else:
        text = " ".join(splitted).lower()
    return text


def clean_data(data):
    data.dropna(inplace=True)
    data["text"] = data["text"].map(lambda s: clear_commentary(s))
    data.dropna(inplace=True)
    print("cleaned")
    return data


def get_category_from_comment(text):
    """���� ����������� ���������� ����������� �� �������� ��������� �� ������
     � �������������� ����������� ��������� ��������� """
    dict = process.extractOne(text.lower(), stops)
    if dict[1] > 75:
        text = dict[0]
    else:
        text = np.nan
    print("wait")
    return text


def get_category_dataset(data):
    """����������� ��������� � ������ ����������� � ���������"""
    print("remap started. wait")
    data.text = data.text.map(lambda comment: get_category_from_comment(str(comment)))
    print("remap ends")

    data.dropna(inplace=True)

    return data
