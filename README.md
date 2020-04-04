# supportSeattleOrg
supportseattle.org is a website that helps Seattle businesses to advertize their 

---
## Frontend local deployment & testing
T.B.W.
## Backend local deployment & testing

Before following the guide, please check [python virtual environment](https://docs.python.org/3/library/venv.html) and [django documentation](https://docs.djangoproject.com/en/3.0/)

Root of the backend guid is supportSeattleOrg/backend/

1. Install all the requirements by running  
    ~~~
    pip3 install -r requirements.txt
    ~~~
2. Create postgres11 database  
   [postgres 11](https://www.postgresql.org/download/)  
   [postgis](https://postgis.net/install/)

3. Create admin user  
    ~~~
    python manage.py createsuperuser
    ~~~

4. Run Django server  
    ~~~
    python3 manage.py runserver
    ~~~

5. Check admin site
    [localhost:8000/admin](http://localhost:8000/admin/)


