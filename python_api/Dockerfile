# Imagen base de Python
FROM python:3.9-slim

# Instalar dependencias
RUN pip install Flask gunicorn

# Copiar archivos
COPY app.py /app/app.py

# Establecer el directorio de trabajo
WORKDIR /app

# Exponer el puerto 8001
EXPOSE 8001

# Comando de ejecución
CMD ["gunicorn", "-b", "0.0.0.0:8001", "app:app"]
