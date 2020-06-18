# Необходимо написать простой веб-сервер с помощью фреймворка Bottle. 
# Все ошибки приложения должны попадать в вашу информационную панель Sentry. 
# Приложение должно размещаться на Heroku, 
# иметь минимум два маршрута:
# /success, который должен возвращать как минимум HTTP ответ со статусом 200 OK
# /fail, который должен возвращать "ошибку сервера" (на стороне Bottle это может быть просто RuntimeError), то есть HTTP ответ со статусом 500

# bottle сервер - на примере https://github.com/heroku-python/bottle-helloworld
import os
from bottle import route, run
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_dsn = os.environ.get('SENTRY_DSN', "https://bad29cf8f9b649edbd5b6e96762093af@o407218.ingest.sentry.io/5275875")
sentry_sdk.init(
    dsn=sentry_dsn,
    integrations=[BottleIntegration()]
)

@route('/success')  
def success():  
    print("This is success!")  
    return "This is success! TEST_ENV_VAR="+os.environ.get('TEST_ENV_VAR')

@route('/fail')  
def fail(): 
    raise RuntimeError("This is a failure!")  

if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 8080)

    # Run the app.
    run(host='0.0.0.0', port=port)