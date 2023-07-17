from fastapi import APIRouter, Response
from config.database import connection
from schemas.authors import authorEntity, authorsEntity
from models.author import Author
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

author = APIRouter()

@author.get('/authors')
def getAuths():
    return authorsEntity(connection.local.author.find())

@author.post('/authors')
def createAuths(auth: Author):
    # Convertimos el auth en un diccionario (o en algo que lo haga procesable)
    new_quote = dict(auth)
    
    # Si quieres enviar encriptado un campo haz esto
    # new_quote["password"] = sha256_crypt.encrypt(new_quote["password"])
    
    del new_quote["id"]
    
    #  local: schema de mongo || author: table of schema local
    id = connection.local.author.insert_one(new_quote).inserted_id
    
    # buscamos cada cita por el "_id" y traemos todos los datos relacionados
    author = connection.local.author.find_one({"_id": id})
    return authorEntity(author)

# recibimos un id: string como parametro con el que buscamos en la BD
@author.get('/authors/{id}')
def findAuthor(id: str):
    return authorEntity(connection.local.author.find_one({"_id": ObjectId(id)})) 

@author.put('/authors/{id}')
def updateAuth(id: str, author: Author):
    connection.local.author.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(author)})
    # El objeto {"$set": dict(auth)} Establece los campos nuevos atraves de auth
    return authorEntity(connection.local.author.find_one({"_id": ObjectId(id)}))

@author.delete('/authors/{id}')
def deleteAuths(id: str):
    authorEntity(connection.local.author.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)