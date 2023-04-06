step1: create virtualenv
>python -m venv env
step2: activate environment
>.\env\scripts\activate
step3:install dependencies
>pip install -r dependancies.txt
step4: run server
>python manage.py runserver
step5: access the below api's

POST: http://127.0.0.1:8000/api/register/

POST: http://127.0.0.1:8000/api/login/

POST,PUT, GET, DELETE : http://127.0.0.1:8000/api/products


