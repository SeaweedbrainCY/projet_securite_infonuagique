FROM debian:bullseye

WORKDIR /code

# Installation des dépendances nécessaires
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Copie des fichiers nécessaires
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir -r /code/requirements.txt
COPY main.py /code/main.py
COPY rename.sh /code/rename.sh
RUN chmod +x /code/rename.sh

# Création du répertoire media et ajustement des permissions
RUN mkdir -p /code/media/
RUN chown -R 101:101 /code

# Exposition du port
EXPOSE 9000

# Changement de l'utilisateur par défaut
USER 101

# Commande par défaut
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
