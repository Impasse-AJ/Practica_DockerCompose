# Imagen base de Node.js
FROM node:14

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos de la aplicación
COPY package.json /app/
COPY app.js /app/

# Instalar dependencias
RUN npm install

# Exponer el puerto 8002
EXPOSE 8002

# Comando de ejecución
CMD ["npm", "start"]