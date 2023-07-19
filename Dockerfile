# imagen de Python
FROM python:3.9

# para no generar archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Deshabilita el búfer de salida (stdout y stderr) para que la salida aparezca en tiempo real
ENV PYTHONUNBUFFERED 1

# Instala las dependencias de la aplicación
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . /app

# Expone el puerto 8000 (o el que esté configurado en la aplicación)
EXPOSE 8000

# Inicio el servidor Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
