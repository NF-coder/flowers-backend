FROM python:3.12.8-slim
LABEL maintainer="@ReshNF"

COPY ./service .
COPY ./start.sh .
COPY ./reqrments.txt .

RUN pip install --upgrade pip
RUN pip install -r reqrments.txt

EXPOSE 50511
EXPOSE 50512
EXPOSE 50513
EXPOSE 50514
EXPOSE 50515
EXPOSE 50516

CMD bash start.sh