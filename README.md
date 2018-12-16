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



