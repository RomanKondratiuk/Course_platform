FROM python:3

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

COPY . .

#RUN  python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
