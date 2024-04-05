FROM python:3

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

#COPY scripts/wait-for-it.sh /wait-for-it.sh
#RUN chmod +x /wait-for-it.sh

COPY . .

