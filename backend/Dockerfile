FROM python:3.12.8-slim
LABEL maintainer="@ReshNF"

COPY . .

RUN pip install --upgrade pip
RUN pip install -r reqrments.txt

# problems with reverse proxy...

#RUN sudo apt update
#RUN sudo apt install nginx -y
#RUN sudo rm /etc/nginx/sites-enabled/default
#RUN sudo ln -s ./nginx-reverse-config /etc/nginx/sites-enabled/
#RUN sudo systemctl restart nginx

EXPOSE 8453
EXPOSE 80

CMD fastapi run --port 8453 --host 0.0.0.0