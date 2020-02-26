FROM python:3.7-buster

ADD requirements.txt /app
RUN pip install -r requirements.txt

ADD similarity.py /app
ENTRYPOINT [ "python", "/app/similarity.py" ]