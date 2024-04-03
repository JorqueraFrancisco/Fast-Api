1.- Clonar el proyecto

2.- Ejecutar el comando

docker compose  up -d

3.- entrar al contenedor

docker compose exec fastapi bash

4.- Para levantar el servidor fast api dentro del contenedor

uvicorn main:app --reload --host 0.0.0.0 --port 8000
