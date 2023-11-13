#!/bin/bash

# Vérifiez si les arguments sont fournis
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <old_path> <new_path>"
    exit 1
fi

old_path=$1
new_path=$2

# Renommez le fichier
mv $old_path $new_path