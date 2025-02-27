FROM python:3.12.8-slim
LABEL maintainer="@ReshNF"

COPY . .

RUN pip install --upgrade pip
RUN pip install -r reqrments.txt

#RUN sudo apt update
#RUN sudo rm /etc/nginx/sites-enabled/default
#RUN sudo ln -s ./nginx-config /etc/nginx/sites-enabled/
#RUN sudo systemctl restart nginx

EXPOSE 8450

CMD fastapi run --port 8450 --host 0.0.0.0