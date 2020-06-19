# logger-bottle-sentry-heroku
D2.10 HW logger bottle sentry heroku

Задание:
1. Необходимо написать простой веб-сервер с помощью фреймворка Bottle. 
2. Все ошибки приложения должны попадать в вашу информационную панель Sentry. 
3. Приложение должно размещаться на Heroku, 
иметь минимум два маршрута:
4. /success, который должен возвращать как минимум HTTP ответ со статусом 200 OK
5. /fail, который должен возвращать "ошибку сервера" (на стороне Bottle это может быть просто RuntimeError), то есть HTTP ответ со статусом 500
6. sentry dsn должно браться из переменной окружения SENTRY_DSN

Состав пакета - в виде, приемлемом для heroku:
1. Сервер: "bottle-sentry-heroku.py"
2. Зависимости:  "requirements.txt"
3. Строка запуска: "Procfile"

Размещен на Heroku: https://sergeyne-bottle-sentry.herokuapp.com/

