FROM python:3.12.8-slim
LABEL maintainer="@ReshNF"

COPY ./service .
COPY ./reqrments.txt .

RUN pip install --upgrade pip
RUN pip install -r reqrments.txt

EXPOSE 8453

CMD fastapi run --port 8453 --host 0.0.0.0
