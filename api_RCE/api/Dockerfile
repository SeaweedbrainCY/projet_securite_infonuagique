FROM debian:bullseye

WORKDIR /code

# Installation des dépendances nécessaires
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN addgroup --system recuser && adduser --system --group rceuser

ENV HOME=/home/rceuser
ENV APP_HOME=/home/rceuser/code
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Copie des fichiers nécessaires
COPY ./requirements.txt $APP_HOME/requirements.txt
RUN pip3 install --no-cache-dir -r /code/requirements.txt
COPY main.py $APP_HOME/main.py
COPY rename.sh $APP_HOME/rename.sh
RUN chmod +x $APP_HOME/rename.sh

RUN chown -R rceuser:rceuser $APP_HOME

# Exposition du port
EXPOSE 9000

# Changement de l'utilisateur par défaut
USER rceuser

# Commande par défaut
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
