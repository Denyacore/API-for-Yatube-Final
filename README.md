# API for Yatube by [Denyacore](https://github.com/Denyacore)

Проект для продвинутых и современных блогеров без границ, 
которые не хотят зацикливаться на одном устройстве, в желании поделиться своими мыслями с миром!

В данном репозитории представлены решения для подключения Yatube к различным системам 
для хранения и обработки текстовых файлов, с возможностью прикрепления и просмотра графических изображений.


## Tech Stack

**Client:** Python 3.7
- djangorestframework 3.12.4,
- djangorestframework-simplejwt 4.7.2,
- Pillow 8.3.1,
- requests 2.26.0,
- pytest 6.2.4
- pytest-django 4.4.0
- PyJWT 2.1.0
- pytest-pythonpath 0.7.3

**Server:** Django 2.2.16


## Authors

- [Denyacore](https://github.com/Denyacore)


## Deployment

To deploy this project run

### How to launch a project:

Clone the repository and go to it on the command line:

```
https://github.com/Denyacore/api_final_yatube.git
```

```
cd api_final_yatube
```

Create and activate a virtual environment:

```
python3 -m venv env
        or
py -m venv venv
```

```
source venv/Scripts/activate
```

```
python3 -m pip install --upgrade pip
                or
py -m pip install --upgrade pip
```

Install dependencies from a file *requirements.txt* :

```
pip install -r requirements.txt
```

Make migrations:

```
python3 manage.py migrate
            or
py manage.py migrate
```

5. Launch a project:

```
python3 manage.py runserver
            or
py manage.py runserver
```

## API Reference

Documentation is available at the link http://127.0.0.1:8000/redoc/

#### Example requests:

```http
POST http://127.0.0.1:8000/api/v1/posts/
GET http://127.0.0.1:8000/api/v1/follow/
```
## Acknowledgements
:pray: :pray: :pray:
 - [Dmitry Lifanov ](https://github.com/Dimalright) for your patience :heart:
 - [Sergey Efanov]() for the ability to explain :books:
 - [Maxim Mityagin]() for for the transfer of experience :sunglasses:
