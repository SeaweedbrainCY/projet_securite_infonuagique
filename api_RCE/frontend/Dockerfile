# Utilisez l'image Nginx Alpine
FROM nginx:alpine

# Copiez les fichiers index.html et malicious.html dans le répertoire par défaut de Nginx
COPY index.html /usr/share/nginx/html/

# Exposez le port 4200
RUN  touch /var/run/nginx.pid && \
     chown -R nginx:nginx /var/cache/nginx /var/run/nginx.pid
USER nginx