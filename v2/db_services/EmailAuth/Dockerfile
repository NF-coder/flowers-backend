FROM python:3.12.8-slim
LABEL maintainer="@ReshNF"

COPY ./service .
COPY ./reqrments.txt .

RUN pip install --upgrade pip
RUN pip install -r reqrments.txt

EXPOSE 50502

CMD python EmailAuth.py