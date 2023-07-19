# Usa la imagen oficial de Python como base
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .

# Instala las dependencias en el contenedor
RUN pip install -r requirements.txt

# Copia el resto de los archivos al contenedor
COPY . .

# Expone el puerto 80 para que sea accesible desde el exterior
EXPOSE 80

# Ejecuta el servidor FastAPI usando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
