# Quasar
MVP онлайн консультанта для ответов на вопросы по проведению закупочных процедур в компании Росатом, что позволить ускорить процесс проведения закупочных процедур. 

### Стэк:
- Langchain
- Gigachain
- GigaChat
- Eel

### Инструкция для запуска
Для запуска desktop приложения необходимо установить зависимости:
```
pip install -r requirements.txt
```

После этого надо запустить файл main.py:
```
python3 main.py
```

Запускается графический интерфейс:

![](./img/screenshot.png)

### Для тестирования telegram бота
Перейдите по ссылке https://t.me/QuasarAstrumBot

### Как запустить telegram бота
Для запуска telegram бота приложения необходимо установить зависимости:
```
pip install aiogram
pip install python-decouple
```

Вставить свой API KEY в файл .env

После этого запустить файл bot.py:
```
python3 bot.py
```
