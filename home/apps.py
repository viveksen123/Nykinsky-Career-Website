from django.apps import AppConfig
from flask import Flask
app = Flask(__name__)



class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

