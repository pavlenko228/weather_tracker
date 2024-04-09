Для создания этого проекта вам необходимо создать env и подключить к ней все необходимые библиотеки:
pip install django
pip install requests
после чего внутри папки проекта создадим основную папку 
django-admin startproject weather_tracer
потом переходим непосредственно в эту папку
cd weather_tracker
в ней уже создаем папку приложения
python manage.py startapp weather
после того, как код будет перенесен в ваш проект, выполним миграцию
python manage.py makemigrations
python manage.py migrate
затем создадим superuser, так как он понадобится нам для реализации логики
python manage.py createsuperuser
после чего заполняем форму прямо в консоли
теперь запустим сервер 
python manage.py runserver
потом зайдем по адрису /admin, где войдем в учетную запись admin, оттуда мы будем иметь доступ к модели с городами, погоду в которых нужно узнать
