# Сайт афиша мероприятий

Используя этот репозиторий можно развернуть сайт с афишей мероприятий.

### Как установить

Должны быть предустановлены Python 3 и pip.

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
Создайте и выполните миграции
```commandline
python manage.py makemigrations

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

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
