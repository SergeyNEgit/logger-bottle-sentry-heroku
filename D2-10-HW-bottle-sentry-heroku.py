# Необходимо написать простой веб-сервер с помощью фреймворка Bottle. 
# Все ошибки приложения должны попадать в вашу информационную панель Sentry. 
# Приложение должно размещаться на Heroku, 
# иметь минимум два маршрута:
# /success, который должен возвращать как минимум HTTP ответ со статусом 200 OK
# /fail, который должен возвращать "ошибку сервера" (на стороне Bottle это может быть просто RuntimeError), то есть HTTP ответ со статусом 500

import sentry_sdk

from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://bad29cf8f9b649edbd5b6e96762093af@o407218.ingest.sentry.io/5275875",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route('/success')  
def success():  
    print("This is success!")  
    return

@app.route('/fail')  
def fail():  
    raise RuntimeError("This is a failure!")  

app.run(host='localhost', port=8080)