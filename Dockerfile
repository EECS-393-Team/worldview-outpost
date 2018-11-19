FROM python:3.6

WORKDIR outpost

COPY . /outpost

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME World

ENV FLASK_APP outpost

CMD ["flask", "run"]
