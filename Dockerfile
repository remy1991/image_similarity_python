FROM python:3.7-buster

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY similarity.py /app/similarity.py
ENTRYPOINT [ "python", "/app/similarity.py" ]
