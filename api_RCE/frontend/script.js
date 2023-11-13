function uploadFile() {
    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];

    if (file) {
        var formData = new FormData();
        formData.append('file', file);

        fetch('http://127.0.0.1:9000/uploadfile/', {
            method: 'POST',
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                renameFile(file.name)
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while uploading the file.');
            });
    } else {
        alert('Please select a file to upload.');
    }
}

function renameFile(filename) {
            var nameInput = document.getElementById('name');
            var name = nameInput.value.trim();

            if (name !== '') {
                fetch(`http://127.0.0.1:9000/renamefile/${filename}/${name}/`, {
                    method: 'PUT',
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    location.reload();
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An error occurred while renaming the file.');
                });
            } else {
                alert('Please enter both old and new file names.');
            }
        }

         // Fonction pour récupérer la liste des fichiers depuis l'API
        async function getFileList() {
            try {
                const response = await fetch('http://127.0.0.1:9000/listfiles/');
                const data = await response.json();
                return data.files;
            } catch (error) {
                console.error('Error:', error);
                return [];
            }
        }

        // Fonction pour supprimer un fichier
        async function deleteFile(fileName) {
            try {
                const response = await fetch(`http://127.0.0.1:9000/deletefile/${fileName}/`, {
                    method: 'DELETE',
                });
                const data = await response.json();
                console.log(data.message);
                updateFileList(); // Mettre à jour la liste après la suppression
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while deleting the file.');
            }
        }

        // Fonction pour mettre à jour la liste HTML avec la liste des fichiers
        async function updateFileList() {
            const fileListElement = document.getElementById('fileList');
            const files = await getFileList();

            // Effacer la liste actuelle
            fileListElement.innerHTML = '';

            // Ajouter chaque fichier à la liste
            files.forEach(file => {
                const row = document.createElement('tr');

                // Nom du fichier
                const fileNameCell = document.createElement('td');
                fileNameCell.textContent = file;
                row.appendChild(fileNameCell);

                // Bouton Supprimer
                const deleteButtonCell = document.createElement('td');
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Supprimer';
                deleteButton.addEventListener('click', () => deleteFile(file));
                deleteButtonCell.appendChild(deleteButton);
                row.appendChild(deleteButtonCell);

                fileListElement.appendChild(row);
            });
        }

        // Appeler la fonction pour mettre à jour la liste lors du chargement de la page
        window.onload = updateFileList;