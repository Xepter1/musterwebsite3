FROM nginx:alpine

# Static site — nur die nötigen Dateien ins Image
COPY default.conf /etc/nginx/conf.d/default.conf
COPY index.html   /usr/share/nginx/html/
COPY assets       /usr/share/nginx/html/assets

EXPOSE 80
