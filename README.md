#### start django   
    virtualenv venv        
    source venv/bin/activate          
    cd mysite          
    python manage.py runserver        

#### setup env  
    pip install virtualenv     
    virtualenv venv     
    source venv/bin/activate   
    pip install Django     
    pip install djangorestframework   
    pip freeze > requirements.txt    
    pip install -r requirements.txt      

#### setup new project
    django-admin startproject django_api    
    cd django_api

    python manage.py migrate
    python manage.py createsuperuser

#### setup new app
    python manage.py startapp languages
    python manage.py makemigrations
    python manage.py migrate
    
    
#### reference
[1] [Getting Started With Django REST Framework](https://www.youtube.com/watch?v=263xt_4mBNc)      
[2] [How to write an API in 3 lines of code with Django REST framework](https://medium.com/crowdbotics/how-to-write-an-api-in-3-lines-of-code-with-django-rest-framework-59b0971edfa4)    




