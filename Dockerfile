
FROM python:3.8.4

COPY . /AutoSUC
WORKDIR /AutoSUC

RUN pip install -r requeriments.txt
RUN echo "MODE='prod'" > AutoSUC/mode.py

CMD python3 manage.py runserver 127.0.0.1:80