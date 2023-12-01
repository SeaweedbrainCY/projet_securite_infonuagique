FROM debian:bullseye

WORKDIR /code

# Installation des dépendances nécessaires
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN addgroup --system badauthuser && adduser --system --group badauthuser

ENV HOME=/home/badauthuser
ENV APP_HOME=/home/badauthuser/code
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Copie des fichiers nécessaires
COPY ./requirements.txt $APP_HOME/requirements.txt
RUN pip3 install --no-cache-dir -r $APP_HOME/requirements.txt
COPY main.py $APP_HOME/main.py

RUN chown -R badauthuser:badauthuser $APP_HOME

# Exposition du port
EXPOSE 80

# Changement de l'utilisateur par défaut
USER badauthuser

# Commande par défaut
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:80", "-k" ,"uvicorn.workers.UvicornWorker"]