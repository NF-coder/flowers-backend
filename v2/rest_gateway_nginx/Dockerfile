FROM nginx:latest
LABEL maintainer="@ReshNF"

COPY . .

# problems with reverse proxy...
RUN apt update
RUN apt install nginx -y
RUN ln -s ./nginx-reverse-config /etc/nginx/sites-enabled/
RUN systemctl restart nginx

# for nginx
EXPOSE 80