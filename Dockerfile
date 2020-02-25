FROM python:3

RUN pip install pillow
RUN pip install imagehash

ADD similarity.py /
ENTRYPOINT [ "python", "/similarity.py" ]