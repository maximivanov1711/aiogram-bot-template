from environs import Env
from os import environ

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

# webhook settings
WEBHOOK_URL = environ.get("WEBHOOK_URL")

# webserver settings
WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(environ.get("PORT"))

