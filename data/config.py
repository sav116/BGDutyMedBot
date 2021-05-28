from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

# URLs for download
URL_GOOGLE_DOC_DEV = env.str("GOOGLE_DOC_DOWNLOAD_DEV")
URL_GOOGLE_DOC_SUP = env.str("GOOGLE_DOC_DOWNLOAD_SUP")