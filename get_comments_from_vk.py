import re
import time
import pandas
import pandas as pd

import lp
import vk_api
import check_correctness


def auth():
    vk_session = vk_api.VkApi(lp.login, lp.password)
    vk_session.auth()
    vk = vk_session.get_api()
    return vk

def getDataFromComments(vk):
    #id группы из которой берем пост
    groupID = "-96717639"#-96717639

    #получаем последний пост в группе
    posts = vk.wall.get(owner_id=groupID, offset=1, count=68)
    print("\n")
    data = pd.DataFrame(columns=['text', 'post_id', "date", "day_in_week", "hour","minute", "day_in_month"])

    # print(posts)
    # print(posts[0])
    for post in posts.get("items"):
        #получаем id последнего поста в группе
        postID = post.get("id")

        # print("post id is "+str(postID))
        if "Всем удачного дня, платите за проезд и не попадайтесь контролю" not in post.get("text"):
            continue
        # print("text is "+str(post.get("text")))

        #получаем объект commentary чтобы из него вытащить число комментариев
        comments = vk.wall.getComments(owner_id=groupID, post_id=postID, count=200)

        # проходимся по массиву комментариев и достаем всё что нужно в dataframe
        for comment in comments.get("items"):

            text = comment.get("text")
            text = re.sub(r"A-Za-zА-Яа-я0123456789 ", "", str(text))
            # print(text)
            commentaryIsNice = check_correctness.detection(text)
            # print(commentaryIsNice)
            if commentaryIsNice:
                print(text)
                date = comment.get("date")
                time_struct = time.gmtime(date)
                post_id = comment.get("post_id")
                data = data.append({"text": text, "post_id" : post_id,
                                    "date": date,"day_in_week" : time_struct.tm_wday,
                                    "hour": (time_struct.tm_hour+3),
                                    "minute": time_struct.tm_min,
                                    "day_in_month": time_struct.tm_mday}, ignore_index=True)


    # print(data[:10])
    # print(data.info())
    data["text"] = data.text.map(lambda s: "университет" if s=="скорина" else s)
    data["text"] = data.text.map(lambda s: "университет" if s=="ггу" else s)
    data["text"] = data.text.map(lambda s: "площадь ленина" if s=="площадь" else s)
    data["text"] = data.text.map(lambda s: "площадь ленина" if s=="ленина" else s)

    # data.to_csv("commentary_dataset.csv", encoding="windows-1251")
    print("dataset is ready")
    return data