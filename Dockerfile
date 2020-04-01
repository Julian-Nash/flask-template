FROM python:3.8.1

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt
RUN pip install .

EXPOSE 8080

CMD [ "uwsgi", "run.ini" ]