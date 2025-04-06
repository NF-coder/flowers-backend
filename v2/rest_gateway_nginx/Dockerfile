FROM nginx:latest
LABEL maintainer="@ReshNF"

COPY nginx-reverse.conf /etc/nginx/conf.d/default.conf
COPY certs/ /etc/nginx/certs/

# for nginx
#EXPOSE 80
EXPOSE 443