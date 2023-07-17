# Encargado de interuactuar con la base de datosfrom

from pydantic import BaseModel
from typing import Optional

class Author(BaseModel):
    author: str
    content: str
    source: Optional[str]