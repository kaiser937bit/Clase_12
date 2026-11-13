from fastapi import FastAPI
from super_db.py import usuarios, items

app = FastAPI()

@app.get("/id")
def get_usuario(id):

