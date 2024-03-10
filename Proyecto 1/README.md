# Proyecto 1

## Integrantes

- **Sergio Córdoba**
- **Miguel Jaramillo**
- **Miguel Sosa**

## Marco Teórico

- **GFS (Google File System):** GFS es el sistema de archivos distribuidos que usa Google. Su estructura es la siguiente. Cada cluster contiene un _master_ y múltiples _chunckservers_ que son accedidos por múltiples _clientes_. Cada chunkserver tiene _chunks_ dentro de él, que son las particiones donde están ubicados los archivos. El master constantemente verifica que haya tres réplicas de cada chunk en diferentes chunckservers, por eso, a la hora de que un chunkserver falle, el master se encarga de crear una replica de cada chunk que hubiera en ese chunkserver para que vuelva a haber 3 de ellas.

  Un aspecto importante es que el master **nunca** escribe ni lee archivos, solo le dice al cliente a que chunkserver se debe conectar.

  Otro componente importante del sistema es el _operational log_, que es un archivo que tiene la información de los archivos, incluyendo cosas como la ubicación del archivo, su tamaño y en que chunkservers se encuentra ubicado.

  Ahora, con respecto al proceso de lectura, el cliente le pregunta al master de donde puede leer el archivo, el master le devuelve las direcciones de los 3 chunkservers para que el cliente haga la consulta. Si alguno de los chunkservers no se encuentra disponible el cliente puede simplemente acceder a otra réplica ya que tiene la dirección de las 3.

  Y con el proceso de escritura, el cliente le pide al master en que chunkserver puede escribir, que se denominará el _chunkserver primario_, y este será el encargado de escribir en los otros chunks para que todos tengan la misma información, todo este proceso ocurre de manera lineal.
