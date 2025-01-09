docker stop contenedir_mpi
docker rm contenedir_mpi
docker build -t mi_primera_imagen .
docker run -d -p 8001:8001 -d --name contenedir_mpi mi_primera_imagen