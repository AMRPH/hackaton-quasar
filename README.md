# Quasar
MVP онлайн консультанта для ответов на вопросы по проведению закупочных процедур в компании Росатом, что позволить ускорить процесс проведения закупочных процедур. 

### Стэк:
- Langchain
- Gigachain
- GigaChat
- Eel

### Инструкция дял запуска
Для запуска desktop приложения необходимо установить зависмости:
```
pip install -r requirements.txt
```

После этого надо запусть файл main.py:
```
python3 main.py
```

Запускается графический интерфейс:

![](./img/screenshot.png)


### Как запустить telegram бота
Для запуска telegram бота приложения необходимо установить зависмости:
```
pip install aiogram
```

Вставить свой API KEY в файл API_BOT_KEY.py

После этого запустить файл bot.py:
```
python3 bot.py
```