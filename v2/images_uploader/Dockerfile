FROM python:3.12.8-slim
LABEL maintainer="@ReshNF"

COPY . .

RUN pip install --upgrade pip
RUN pip install -r reqrments.txt

EXPOSE 8450

CMD fastapi run --port 8450 --host 0.0.0.0