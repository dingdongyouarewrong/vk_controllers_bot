import re

#ищем знаки смайлики и всё что не относится к тексту
def testForQuestion(text):
    match = re.match("^[-абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789,. )(]*$", text.lower())
    if match is not None:
        return 0
    else:
        return 1

#ищем слово "есть"
# def testForHere(text):
#     try:
#         if (text.index("есть")):
#             return 1
#     except ValueError:
#         return 0

#ищем слова "чисто", "уехали","свалили"
def testForClear(text):
    if ("чисто" in text.lower() or
            "уехали" in text.lower() or
            "свалили" in text.lower() or
            "пусто" in text.lower() or
            "никого" in text.lower() or
            "как там" in text.lower() or
            "автобус" in text.lower() or
            "подскажите" in text.lower() or
            "кто" in text.lower() or
            "что" in text.lower() or
            ("как" in text.lower() and "от" in text.lower())):
        return 1
    else:
        return 0

def detection(text):

    #если что-то не так, ошибка прибавляется по одному за каждый признак
    error = 0
    error = error + testForQuestion(text)
    # error = error + testForHere(text)
    error = error + testForClear(text)

    # print(str(error)+" errors")

    if error==0:
        return True
    else:
        # print("shit \n\n")
        return False



