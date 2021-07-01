# Задача 2. Функция обратного вызова
# При работе с сетью и веб-сервисами иногда используется так называемая функция обратного вызова — это функция, которая вызывается при срабатывании определённого события (переходе на страницу, получении сообщения или окончании обработки процессором). В неё можно передать функцию, чтобы она выполнилась после определённого события. Это используется, например, в HTTP-серверах в ответ на URL-запросы. Реализуйте такую функцию.
#
#
#
# Пример функции:
#
# @callback('//')
#
# def example():
#
#     print('Пример функции, которая возвращает ответ сервера')
#
#     return 'OK'
#
#
#
# Основной код:
#
# route = app.get('//')
#
# if route:
#
#     response = route()
#
#     print('Ответ:', response)
#
# else:
#
#     print('Такого пути нет')
#
#
#
# Ожидаемый результат:
#
# Пример функции, которая возвращает ответ сервера
#
# Ответ: OK