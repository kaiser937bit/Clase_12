from fastapi import FastAPI
from super_db import usuarios, items
#import super_db

app = FastAPI()

@app.get("/usuario/{id}")
def get_usuario(id: int):
    usuario = usuarios.get(id)
    print(usuario)
    return usuario