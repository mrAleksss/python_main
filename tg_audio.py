import telegram
import os
import requests


def send_audio_file(bot, chat_id, file_name):
    with open(file_name, 'rb') as f:
        bot.send_audio(chat_id, f)
    os.remove(file_name)
    
# Инициализируем бота
bot = telegram.Bot(token='YOUR_TELEGRAM_BOT_TOKEN')

# Отправляем mp3 файл
send_audio_file(bot, chat_id, 'filename.mp3')



def send_audio_url(bot, chat_id, url):
    response = requests.get(url, stream=True)
    bot.send_audio(chat_id, response.raw)

# Инициализируем бота
bot = telegram.Bot(token='YOUR_TELEGRAM_BOT_TOKEN')

# Отправляем mp3 с интернета
send_audio_url(bot, chat_id, 'http://example.com/filename.mp3')
```
