##### POSTWORK
## BASES DE DATOS SQL EN PYTHON APLICADO A PROYECTO PERSONAL

### OBJETIVOS
 - Obtener un modelo de base de datos.
 - Inicializar la base de datos en MariaDB.
 - Crear cuando menos una de las tablas del modelo en la base de datos usando SQL.
 - Agregando algunos datos a la tabla creada haciendo uso de de SQL.
 - Listar los registros de una tabla desde un script en Python.
 - Agregar registros a una tabla haciendo uso de un script en Python.

#### REQUISITOS
1. Contar con la descripción del proyecto en no más de una cuartilla.

1. Usar la carpeta de trabajo `Clase-05/Postwork`

   ```sh
   $ cd Clase-05/Postwork

   Clase-05/Postwork $
   ```

### DESARROLLO
1. __DIAGRAMA DE TABLAS__ Obtener el diagrama de las tablas adecuadas para su proyecto, cuando menos deberá de constar con una foto del diagrama realizado en papel o se puede usar cual software de diagramación o diseño.

   __Diagrama resultante:__

   [TÚ DIAGRAMA]   
   ***

1. __INICIALIZAR LA BASE DE DATOS__ Este paso es muy similar al realizado en el Reto-02, sólo que en lugar de usar el archivo `bedutravels.sql`, ahora se usará el archivo `sql/proyecto.sql`.

  __Comando a ejecutar para el caso de Docker en Linux o Mac:__
  ```sh
  Clase-05/Postwork $ sudo docker exec -i pythonsql mysql -hlocalhost -uroot -ppythonsql < sql/proyecto.sql  
  ```

  __Comando a ejecutar para el caso de Docker en Windows:__
  ```sh
  Clase-05/Postwork > docker exec -i pythonsql mysql -hlocalhost -uroot -ppythonsql < sql/proyecto.sql  
  ```

  __Comando a ejecutar para el caso de MySQL:__
  ```sh
  Clase-05/Postwork $ mysql -hlocalhost -uroot -ppythonsql < sql/proyecto.sql  
  ```
  ***

1. __CREACIÓN DE TABLAS__ Para este paso seguir las instrucciones del Reto-03 pero creando alguna o varias de las tablas de tu diagrama.

  __La conexión a la base de datos se realiza con:__
  ```sh
  Clase-05/Postwork $ sudo docker exec -it pythonsql mysql -hlocalhost -uProyecto -pProyecto Proyecto
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
  Remplazar NombreTabla y ListaCampos por valores acorder a tú proyecto.
  ***

1. __CRUD DE DATOS EN SQL__ Para este paso seguir las instrucciones del Reto-04 pero con datos para tú proyecto.

  __Insertando datos a la tabla NombreTabla:__
  ```sql
  MariaDB [Proyecto]> INSERT INTO NombreTabla VALUES (null, ListaValores);

  [... más instrucciones SQL]

  MariaDB [Proyecto]>
  ```
  ***

1. __CRUD DE DATOS EN PYTHON__ Para este paso seguir las instrucciones del Proyecto y realiza cuando menos las operaciones __READ__ y __CREATE__ para cuando menos una tabla de tu proyecto.

  __Listando registros de una tabla:__
  ```sh
  Clase-05/Postwork $ python lista-registros.py NombreTabla
  [Lista de registros]
  ```

  __Agregando un registro a una tabla:__
  ```sh
  Clase-05/Postwork $ python agrega-nombretabla.py ListaValores
  [Mensale del registro agregado]
  ```
  ***
