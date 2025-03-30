# Переводчик текста
Данный сервис предназначен для определения языка текста, перевода и аудирования


### Алгоритм действия пользователя
Для пользования сервисом необходима регистрация или авторизация
* После авторизации пользователь вводит текст для перевода в поле
* Система определяет язык перевода, переводит и предлагает прослушать перевод и оригинал текста
* Перевод (в том числе и mp3-файл) сохраняется в БД

### Личный кабинет
Все зарегистрированные пользователи имеют свой личный кабинет пользователя.
При переходе в личный кабинет пользователи видят все свои переводы текстов
* Каждый перевод можно либо удалить либо перейти по ссылке для детального просмотра
* Детальный просмотр предоставляет возможность просмотреть перевод текста
* Скачать в Word перевод текста и оригинал текста для сравнения
* Скачать файл оригинала текста и переведенный текст в формате mp3 для дальнейшего прослушивания

## Запуск тестов
Для запуска тестов необходимо из папки проекта выполнить команду
```bash
poetry run pytest
```

## Makefile

Отключить pre-commit
```bash
make pre-commit_off
```

Включить pre-commit
```bash
make pre-commit_on
```

Проверить проект flake8
```bash
make lint
```

Сортировка всех импортов
```bash
make isort
```