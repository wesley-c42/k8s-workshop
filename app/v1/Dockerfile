FROM python:3.8-slim

COPY . /

RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

CMD ["python","run.py"]