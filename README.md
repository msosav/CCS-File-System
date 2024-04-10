# Proyecto 1

## Integrantes

- **Sergio Córdoba**
- **Miguel Jaramillo**
- **Miguel Sosa**

## Descripción

Un sistema de archivos distribuidos permite compartir y acceder de forma concurrente un conjunto de archivos almacenados en diferentes nodos. Uno de los sistemas más maduros, vigente y antiguo de estos sistemas es el NFS (Network File System) desarrollado en su momento por Sun Microsystems y que hoy en día es ampliamente usado en sistemas Linux. Hay otros sistemas de archivos distribuidos como AFS (Andrew File System) y SMB (Server Message Block) conocido como CIFS.

En general hay dos acercamientos para el diseño e implementación de un DFS: 1) basado en bloques y basado en objetos.

Los DFS basados en bloques generalmente garantizan 2 aspectos: 1) la unidad de escritura y lectura es a nivel de bloque, y los bloques pueden ser distribuidos en diferentes nodos, la idea es que los bloques de un archivo estén distribuidos en un conjunto de nodos. 2) el sistema operativo cliente de un DFS garantiza transparencia en el sentido de que la API ofrecida desde el SO es igual para acceder archivos locales que remotos, porque el DFS se integra con el sistema de gestión de archivos del sistema operativo (ej: NFS, AFS, SMB, etc).

Los DFS basados en objetos (object storage, ej: AWS S3), los dos aspectos anteriores se manejan así: 1) la unidad de distribución es a nivel de archivo y no de bloque, es decir, y se garantiza que se lee o escribe un archivo como un todo y no a nivel de bloque. No está diseñado como un sistema de acceso aleatorio al archivo sino secuencial. No soporta la operación de actualización parcial del archivo, sino que se debe reemplazar todo el archivo. Son sistemas distribuidos de archivos principalmente diseñado para un enfoque WORM (Read-Once-Read-Many). Típicamente estos DFS soporta altos niveles de escalabilidad, redundancia y rendimiento. Si bien desde el cliente tiene una visión de archivo completo, en el sistema de backend podría tener (y normalmente lo hay) un mecanismo de particionamiento del archivo por bloques u otro criterio para mejorar la escalabilidad, tolerancia a fallos y rendimiento. 2) el sistema operativo local del cliente NO integra directamente la gestión de este DFS y, en vez de ello, se cuenta con un SDK o API para las primitivas de la gestión de archivos y suelen tener su propio CLI.

## Arquitectura

<p align="center">
  <img src="https://github.com/msosav/CCS-File-System/assets/85181687/3ce303fa-3b46-4a13-b845-5fac582a9990" />
</p>

Todas las comunicaciones se harán con gRPC.

## Resolución de los retos

### Particionamiento

Para el particionamiento se usará la misma técnica usada en HDFS (Hadoop distributed file system). El acercamiento que ellos toman es que los archivos se tratan como directorios, y que adentro de ellos se guardan las partes en las que se divide el archivo. Esto facilita la concurrencia a la hora de la escritura debido a que los clientes pueden agregar diferentes partes del archivo en diferentes nodos solo con el indicador de secuencia que el NameNode da, que es part-000x, lo que permite una fácil reconstrucción del archivo.

### Replicación

Para la replicación manejaremos el tener siempre 3 replicas. Además, se utilizará la misma técnica que en Hadoop distributed file system. Esta técnica es que la replicación se hará de manera lineal, el cliente se comunica con el primer dataNode y ya este dataNode se comunica con un segundo dataNode y este segundo se comunica con el tercer y último dataNode para así cumplir con el tener las 3 replicas que especificamos. Esto proporciona diferentes ventajas como lo son la tolerancia a fallos, ya que si un dataNode falla hay al menos otros dos que tienen la información que esta tenia, también ayuda a la disponibilidad, porque si necesitan leer una partición varios clientes, podrán leerlo de distintos dataNodes a la vez.

### Mantener el directorio o sistema de archivos.

Para el sistema de archivos utilizamos una comunicación de tipo gRPC entre el Cliente y el NameNode, en donde el Cliente solicita al NameNode la lista de archivos existentes y este le devuelve una respuesta gRPC que contiene el nombre del archivo y los KB (usando el comando “ls”).

## Protocolos

### NameNode

- **Create:** se encarga de crear un archivo
- **ListFiles:** se encarga de listar los archivos
- **ReplicationURL:** se encarga de realizar una solicitud a la URL
- **SaveNodeFile:** se encarga de guardar que un data node tiene un archivo
- **DeleteNodeFile:** se encarga de eliminar un archivo
- **HeartBeat:** se encarga de realizar un “latido” para ver los DataNodes activos
- **Download:** se encarga de descargar un archivo

### DataNode

- **SendPartition:** se encarga de enviar una partición
- **DownloadPartition:** se encarga de descargar una partición
- **Replicate:** se encarga de replicar una partición

## Despliegue

### NameNode

Para desplegar el sistema de archivos distribuido se debe seguir los siguientes pasos (con Docker instalado):

1. Hacerle pull a la imagen de NameNode:

```bash
docker pull msosav/ccs-file-system-namenode:latest
```

2. Correr el contenedor de NameNode:

```bash
docker run -d -p 8080:8080 msosav/ccs-file-system-namenode
```

### DataNode

Para desplegar el sistema de archivos distribuido se debe seguir los siguientes pasos (con Docker instalado):

1. Hacerle pull a la imagen de DataNode:

```bash
docker pull msosav/ccs-file-system-datanode:latest
```

2. Correr el contenedor de DataNode:

```bash
docker run -d -p 50051:50051 -e SERVER_IP="12.34.56.7" -e SELF_IP="12.34.56.7" msosav/ccs-file-system-datanode
```

### Cliente

Para desplegar el sistema de archivos distribuido se debe seguir los siguientes pasos (con Docker instalado):

1. Hacerle pull a la imagen de Cliente:

```bash
docker pull msosav/ccs-file-system-cliente:latest
```

2. Correr el contenedor de Cliente:

```bash
docker run -it -d -e SERVER_IP="12.34.56.7" msosav/ccs-file-system-cliente
```

3. Para ejecutar el cliente:

```bash
docker exec -it <container_id> bash
pipenv run python cliente.py
```
