FROM --platform=linux/amd64 nginx:1.21.4

# SET DIR
RUN mkdir -p /misc/django_api_server/log


# SET CONF
RUN rm -f /etc/nginx/conf.d/default.conf
COPY basic-nginx.conf /etc/nginx/nginx.conf
COPY service-nginx.conf /etc/nginx/conf.d
COPY jwt.js /etc/nginx/jwt.js


# SET ENTRYPOINT
COPY entrypoint.sh /entrypoint.sh
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /entrypoint.sh
RUN chmod +x /wait-for-it.sh