
# Описание

Программа позволяет автоматизировать сбор фотографий с сайтов SpaceX и NASA и публиковать их в Telegram-канале. Для публикации фотографий в Telegram нужно создать бота и создать Telegram-канал, где бот станет администратором.

## Как установить 

Скачайте репозиторий на пк, а затем используйте `pip` для установки зависимостей:
```
pip install -r requirements.txt
```
## Переменнные окружения

создайте файл .env и присвойте значения переменным окружения: `NASA_API_KEY`, `TELEGRAM_BOT_TOKEN` и `PUBLICATION_INTERVAL`(интервал между автоматическими публикациями фото в Telegram-канале). Для доступа к API NASA вам понадобится ключ API. Сгенерируйте ключ `NASA_API_KEY` по [ссылке](https://api.nasa.gov/). Чтобы сгенерировать токен доступа к Telegram-боту, вам нужно поговорить с @BotFather и выполнить несколько простых шагов (описанных [здесь](https://core.telegram.org/bots#6-botfather)).

## Запуск скрипта fetch_spacex_photos.py
 
 Скрипт скачивает с сайта SpaceX в папку images фотографии последнего запуска или определенного запуска, используя идентификатор запуска `launch_id` в качестве аргумента. При запуске скрипта в терминале ничего не выводится, а в папке появляются фотографии. Документация (по получению фотографий запусков [здесь](https://github.com/r-spacex/SpaceX-API/blob/master/docs/launches/v5/latest.md).
 
 _Пример:_
```
python .\fetch_spacex_photos.py --launch_id '5eb87d47ffd86e000604b38a'
```
## Запуск скрипта fetch_spacex_photos.py

Скрипт скачивает с сайта NASA в папку images фотографии APOD(Астрономическая картинка дня). Количество скачанных фотографий можно регулировать с помощью аргумента `count`(по умолчанию 30). При запуске скрипта в терминале ничего не выводится, а в папке появляются фотографии. С документацией по APOD API можно ознакомиться [здесь](https://api.nasa.gov/#apod).

 _Пример:_
```
python .\fetch_nasa_apod_photos.py --count 10 
```

## Запуск скрипта fetch_nasa_epic_photos.py

Скрипт скачивает с сайта NASA в папку images фотографии EPIC(Earth Polychromatic Imaging Camera). Количество скачанных фотографий можно регулировать с помощью аргумента `count`(по умолчанию 10). При запуске скрипта в терминале ничего не выводится, а в папке появляются фотографии. С документацией по EPIC API можно ознакомиться [здесь](https://api.nasa.gov/#epic)).

 _Пример:_
```
python .\fetch_nasa_epic_photos.py --count 5
```

## Запуск скрипта spacealbum_telegram_bot.py

Скрипт публикует из заданной директории определенные фотографии, выбранные пользователем, или производит бесконечную автоматическую выгрузку по заданному инвервалу публикаций в Telegram-канал(по умолчанию 1440 секунд). При запуске скрипта в терминале ничего не выводится, а в Telegram-канале появляются фотографии.

 _Пример автоматической загрузки фотографий с интервалом в 10 секунд:_
```
python .\spacealbum_telegram_bot.py --chat_id '@spacealbum' --interval 10
```

 _Пример загрузки определенной фотографии:_
```
python .\spacealbum_telegram_bot.py --chat_id '@spacealbum' --filename apod_9.jpg
```

## Вспомогательный скрипт download_photos.py

Загружает фотографии в папку и возвращает любое расширения файла.
