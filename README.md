Необходимые параметры:
* Токен для работы бота в vk. Получается в настройках группы.
* Логин и пароль пользователя - используется для доступа к комментариям закрытых групп.
* Имя сгенерированного датасета с остановками
* ID группы, из которой парсим комментарии - начинается с -
* ID группы, к которой добавляем бота


Чтобы запустить парс данных, и сразу же бота - задаём параметры и запускаем метод start_service

Чтобы запустить только бота - задаём параметры и запускаем метод start_vk_bot

Перед работой замените логин и пароль на свои в файле lp.py

Статья:
https://habr.com/ru/post/478490/
