# Сайт афиша мероприятий

Используя этот репозиторий можно развернуть сайт с афишей мероприятий.

### Как установить

Должны быть предустановлены Python 3.10+ и pip.

Скачайте код с помощью команды в командной строке
```commandline
git clone https://github.com/Boltasov/dvmn_afisha
```
Перейдите в папку с проектом
```commandline
cd dvmn_afisha
```
Установите необходимые библиотеки командой
```
python pip install -r requirements.txt
```
### Как запустить на локальном компьютере
Подготовьте переменные окружения:
- SECRET_KEY - сгенерируйте свой https://www.makeuseof.com/django-secret-key-generate-new/
- DEBUG - по умолчанию False
- ALLOWED_HOSTS для разработки будет достаточно `localhost, 127.0.0.1`
- STATIC_ROOT по умолчанию `collected_static`

Проверьте наличие миграций и примените миграции
```commandline
python manage.py makemigrations --dry-run --check  

python manage.py migrate
```
Создайте пользователя для админки
```commandline
python manage.py createsuperuser
```
Запустите локальный сервер
```commandline
python manage.py runserver
```

По умолчанию сайт должен быть доступен по адресу http://127.0.0.1:8000/

Чтобы попасть в панель админа откройте http://127.0.0.1:8000/admin

### Как быстро добавить место на карту
Для этого в командной выполните:

```commandline
python manage.py load_place https://raw.githubusercontent.com/Boltasov/dvmn_afisha/master/example_data.json
```

Для загрузки своих данных замените ссылку на файл на свою.


### Посмотреть как будет выглядеть сайт
https://boltasov.pythonanywhere.com/

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
