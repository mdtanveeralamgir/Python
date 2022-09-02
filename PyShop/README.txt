Install django cmd
    - pip install django==2.1 //installing version 2.1

create django project cmd
    - django-admin startproject pyshop .

Folder structure
    - pyshop
        - Settings.py //Define different settings
        - urls.py //Define route
        - wsgi.py //Web server gateway interface, This moduel provides a standard interface between django and server
    - manage.py //To manage django project. start webserver, work with db

Run the server command
    - python3 manage.py runserver

Create a package app cmd
    - python3 manage.py startapp products

Folder structure of products app
    - __init__.py //makes the app a project and can be implemented in other projects
    - admin.py //Define how the admin panel will look like
    - apps.py //Config
    - models.py //define classes of new type for modeling the concepts of new type. like: products,category,review
    - tests.py //automated test
    - views.py //resides views

Registering products app module in python
    - Locate apps.py file in products package
    - app.py is the config file for product package
    - add the path of app.py file in "INSTALLED_APPS" list inside pyshop/settings.py

Migration
    - In models inside products package define the table structure
    - follow steps in "Registering products app module in python"
    - cmd: "python3 manage.py makemigrations" to make the migration file
    - The above command will create a file in products/migration folder containing all the details of creating a table
    - cmd: "python3 manage.py migrate" to run the migration files