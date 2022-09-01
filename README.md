# initial setting guide

- mkdir django-project
- cd django-project
- django-admin startproject django_swagger

# installation guide

## conda deactivate -> venv activate -> install library -> runserver -> http://127.0.0.1:8000/swagger/

```
conda deactivate

sudo apt-get install python3.8-venv

python3 -m venv venv

source venv/bin/activate

python --version -> 3.8.10

pip install django~=3.0

pip install djangorestframework~=3.10

pip install drf-yasg

python manage.py runserver
```
