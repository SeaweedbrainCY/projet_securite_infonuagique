from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Configuration de CORS pour permettre les requêtes depuis n'importe quel origine
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dossier pour stocker les fichiers
media_folder = "media"

# Vérifiez si le dossier media existe, sinon, créez-le
if not os.path.exists(media_folder):
    os.makedirs(media_folder)


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(media_folder, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return JSONResponse(content={"message": "File uploaded successfully"}, status_code=201)


@app.get("/listfiles/")
async def list_files():
    files = [f for f in os.listdir(media_folder) if os.path.isfile(os.path.join(media_folder, f))]
    return JSONResponse(content={"files": files})


@app.put("/renamefile/{old_name}/{new_name}/")
async def rename_file(old_name: str, new_name: str):
    old_path = os.path.join(media_folder, old_name)
    new_path = os.path.join(media_folder, new_name)
    print(old_path, new_path)
    if os.path.exists(old_path):
        # Utilisez un script Bash pour renommer le fichier
        os.system(f"./rename.sh {old_path} {new_path}")
        return JSONResponse(content={"message": f"File {old_name} renamed to {new_name}"})
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.delete("/deletefile/{file_name}/")
async def delete_file(file_name: str):
    file_path = os.path.join(media_folder, file_name)

    if os.path.exists(file_path):
        os.remove(file_path)
        return JSONResponse(content={"message": f"File {file_name} deleted"})
    else:
        raise HTTPException(status_code=404, detail="File not found")