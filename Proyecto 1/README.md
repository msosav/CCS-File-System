# Proyecto 1

## Integrantes

- **Sergio Córdoba**
- **Miguel Jaramillo**
- **Miguel Sosa**

## Marco Teórico

- **GFS (Google File System):** GFS es el sistema de archivos distribuidos que usa Google. Su estructura es la siguiente. Cada cluster contiene un _master_ y múltiples _chunckservers_ que son accedidos por múltiples _clientes_. Cada chunkserver tiene _chunks_ dentro de él, que son las particiones donde están ubicados los archivos. El master constantemente verifica que haya tres réplicas de cada chunk en diferentes chunckservers, por eso, a la hora de que un chunkserver falle, el master se encarga de crear una replica de cada chunk que hubiera en ese chunkserver para que vuelva a haber 3 de ellas.

  Un aspecto importante es que el master **nunca** escribe ni lee archivos, solo le dice al cliente a que chunkserver se debe conectar.

  Otro componente importante del sistema es el _operational log_, que es un registro que tiene la información de los archivos, incluyendo cosas como su dirección, su tamaño y en que chunkservers se encuentra ubicado.

  Ahora, con respecto al proceso de lectura, el cliente le pregunta al master de donde puede leer el archivo, el master le devuelve las direcciones de los 3 chunkservers para que el cliente haga la consulta. Si alguno de los chunkservers no se encuentra disponible el cliente puede simplemente acceder a otra réplica ya que tiene la dirección de las 3.

  Y con el proceso de escritura, el cliente le pide al master en que chunkserver puede escribir, que se denominará el _chunkserver primario_, y este será el encargado de escribir en los otros chunks para que todos tengan la misma información, todo este proceso ocurre de manera lineal.

- **HDFS (Hadoop Distributed File System):** HDFS es un sistema de archivos distribuido creado por Apache y Yahoo!. Su arquitectura está constituida por un _NameNode_ que es el encargado de la localización de los recursos y se asegura que siempre hayan 3 réplicas de cada bloque de archivo. Los _DataNodes_ que se encargan de almacenar los bloques de archivos y de periodicamente mandarle al servidor información de su capacidad de almacenamiento y otros aspectos relevantes para la toma de decisiones.

  Su funcionamiento e implementación es muy similar al GFS, pero hay dos componentes clave que destacan en HDFS, estos son _CheckpointNode_ y _BackupNode_.

  El CheckpointNode es responsable de realizar checkpoints regulares del namespace de HDFS. Esencialmente, el CheckpointNode almacena una copia del namespace en un formato más persistente, lo que ayuda a garantizar la integridad y la eficiencia del sistema.

  El BackupNode es similar al CheckpointNode, este es responsable de mantener una copia actualizada y persistente del namespace de HDFS, pero, a diferencia del CheckpointNode, el BackupNode no solo mantiene un estado consistente del sistema de archivos en disco, sino que también puede asumir temporalmente las responsabilidades de NameNode en caso de fallo de este último. Lo que permite una recuperación más rápida y eficiente del sistema en situaciones críticas.

### Glosario

- **_Sistema de archivos distribuido:_** Es un esquema de almacenamiento y gestión de datos que permite a los usuarios o a las aplicaciones acceder a archivos de datos como PDF, documentos de Word, imágenes, archivos de vídeo, archivos de audio, etc., desde un almacenamiento compartido en cualquiera de los múltiples servidores en red.
- **_Log:_** Es un archivo que registra eventos específicos dentro de un sistema.
- **_Réplica:_** Es la copia que se tiene de un recurso en específico.
- **_Namespace:_** Es una abstracción que permite a los usuarios y aplicaciones interactuar con los archivos y directorios como si estuvieran almacenados en un único sistema de archivos, incluso cuando en realidad están distribuidos en varios servidores o ubicaciones físicas.
- **_Checkpoint:_** Es una copia de seguridad del estado actual de una máquina.

## Referencias

- The Google File System - Sanjay Ghemawat, Howard Gobioff & Shun-Tak Leung
- The Hadoop Distributed File System - Konstantin Shvachko, Hairong Kuang, Sanjay Radia, Robert Chansler
- [¿Qué es el DFS? - Sistema de archivos distribuidos](https://www.nutanix.com/es/info/distributed-file-systems)
- [¿Qué son los logs y para qué sirven?](https://keepcoding.io/blog/que-son-logs-y-para-que-sirven/)
- [Sistemas distribuidos: replicación (IV)](https://medium.com/@edusalguero/sistemas-distribuidos-replicacion-14d8f3819c1d)
