# -*- coding: windows-1251 -*-
from datetime import datetime


def get_stops_by_time(data):
    day = datetime.today().strftime('%w')
    hour = int(datetime.today().strftime('%H'))

    selected_data = data[(data["day_in_week"] == day) & (data["hour"] == hour)]

    return dict(selected_data["text"].value_counts())
