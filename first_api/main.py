from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.author import author

app = FastAPI()

app.add_middleware(
    CORSMiddleware
)

app.include_router(author)