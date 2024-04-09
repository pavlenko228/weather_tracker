1) Для создания этого проекта вам необходимо создать env и подключить к ней все необходимые библиотеки:
    pip install django
    pip install requests
2) После чего внутри папки проекта создадим основную папку 
    django-admin startproject weather_tracer
3) Потом переходим непосредственно в эту папку
    cd weather_tracker
4) В ней уже создаем папку приложения
    python manage.py startapp weather
5) После того, как код будет перенесен в ваш проект, выполним миграцию
    python manage.py makemigrations
    python manage.py migrate
6) Затем создадим superuser, так как он понадобится нам для реализации логики
    python manage.py createsuperuser
7) После чего заполняем форму прямо в консоли
8) Теперь запустим сервер 
    python manage.py runserver
9) Потом зайдем по адрису /admin, где войдем в учетную запись admin, оттуда мы будем иметь доступ к модели с городами, погоду в которых нужно узнать
