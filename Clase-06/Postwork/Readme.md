`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 06`](../Readme.md) > Postwork
## RELACIONES DE BASES DE DATOS SQL EN PYTHON APLICADO A PROYECTO PERSONAL

### OBJETIVOS
 - Obtener un modelo entidad-relación incluyendo cuando menos tres tablas del Proyecto.
 - Crear las tablas y sus relaciones con SQL
 - Agregando datos a las tablas creadas haciendo uso de de SQL o Python
 - Usar un script en Python para imprimir un reporte que incluya datos de cuando menos dos tablas.

#### REQUISITOS
1. Contar con la descripción del proyecto en no más de una cuartilla.
1. Contar con el modelo que incluye sólo tablas, sin relaciones.
1. Usar la carpeta de trabajo `Clase-06/Postwork`

   ```sh
   $ cd Clase-06/Postwork

   Clase-06/Postwork $
   ```

### DESARROLLO
1. __DIAGRAMA DE ENTIDAD-RELACIÓN__ Obtener el diagrama de entidad-relación de las tablas obtenidas anteriormente y en caso de ser necesario agregar o eliminar tablas. Cuando menos deberá de obtener una foto del diagrama realizado en papel o se puede usar cual software de diagramación o diseño (http://draw.io).

   __Diagrama resultante:__

   [TÚ DIAGRAMA]   
   ***

1. __CREACIÓN DE TABLAS__ Para este paso seguir las instrucciones del Reto-03 pero creando las tablas de tu diagrama.

  __La conexión a la base de datos se realiza con:__
  ```sh
  Clase-06/Postwork $ sudo docker exec -it pythonsql mysql -hlocalhost -uProyecto -pProyecto Proyecto
  Welcome to the MariaDB monitor.  Commands end with ; or \g.
  Your MariaDB connection id is 13
  Server version: 10.3.15-MariaDB-1:10.3.15+maria~bionic mariadb.org binary distribution

  Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

  Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

  MariaDB [Biblioteca]>   
  ```

  __La creación de una tabla se realizaría con:__
  ```sql
  MariaDB [Proyecto]> CREATE TABLE NombreTabla (id INTEGER PRIMARY KEY AUTO_INCREMENT, ListaCampos);

  MariaDB [Proyecto]> DESCRIBE NombreTabla;
  [texto con el resultado del comando]

  MariaDB [Proyecto]>
  ```
  Remplazar NombreTabla y ListaCampos por valores acorder a tú proyecto, recuarda ajustar los campos según sea el caso y el tipo de tabla, considera que los campos FK tienen que ser no nulos y en caso de tablas con más de una llave primaria (PK) definir la llave primaria por separado.
  ***

1. __Generando un reporte de tu Proyecto__ Para este paso seguir las instrucciones del Proyecto realizado en clase pero ahora con los datos para tú Proyecto usando un script en Python.

  __Resultado de ejecución del script:__
  ```sh
  Clase-06/Postwork $ python lista-datos.py
  [Lista de registros]
  ```
  ***
