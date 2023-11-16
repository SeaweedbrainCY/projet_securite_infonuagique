# Utilisez l'image Nginx Alpine
FROM nginx:alpine

# Copiez les fichiers index.html dans le répertoire par défaut de Nginx
COPY index.html /usr/share/nginx/html/
COPY index.css /usr/share/nginx/html/
COPY nasa-Q1p7bh3SHj8-unsplash.jpg /usr/share/nginx/html/
COPY connected.css /usr/share/nginx/html/
COPY connected.html /usr/share/nginx/html/
COPY admin.html /usr/share/nginx/html/

EXPOSE 8080
RUN  touch /var/run/nginx.pid && \
     chown -R nginx:nginx /var/cache/nginx /var/run/nginx.pid
USER root