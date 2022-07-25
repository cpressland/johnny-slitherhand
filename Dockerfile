FROM docker.io/python:3.10

WORKDIR /app

ADD logic.py main.py /app/

RUN pip install falcon

CMD ["python", "main.py"]
