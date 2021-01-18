
FROM python:3.8.4

COPY . /AutoSUC
WORKDIR /AutoSUC

RUN pip install -r requeriments.txt

CMD python3 manage.py runserver 0.0.0.0:80