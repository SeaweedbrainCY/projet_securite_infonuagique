# Utilisez l'image Nginx Alpine
FROM nginx:alpine

# Copiez les fichiers index.html dans le répertoire par défaut de Nginx
COPY index.html /usr/share/nginx/html/
COPY index.css /usr/share/nginx/html/
COPY pexels-stephan-seeber-1261728.jpg /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/

EXPOSE 8080
RUN  touch /var/run/nginx.pid && \
     chown -R nginx:nginx /var/cache/nginx /var/run/nginx.pid
USER root