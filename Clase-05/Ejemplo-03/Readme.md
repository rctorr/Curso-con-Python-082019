##### EJEMPLO-03
## CREANDO TABLAS EN MARIADB

### OBJETIVO
Conocer la instrucción para crear una tabla en MariaDB, así como definir el tipo de dato para cada uno de los atributos.

#### REQUISITOS
1. Contar con la base de datos Biblioteca inicializada y con los datos de conexión:

   __Host:__ localhost \
   __User:__ Biblioteca \
   __Password:__ Biblioteca \
   __Base de datos:__ Biblioteca

2. Haber actualizado el contenido de la carpeta `CursoPythonBedu`
3. Abrir una terminal o consola de comandos y cambiarse a la carpeta de trabajo `CursoPythonBedu/Clase-05/Ejemplo-03`

   ```sh
   $ cd Clase-05/Ejemplo-03

   Clase-05/Ejemplo-03 $ ls
   Readme.md

   Clase-05/Ejemplo-03 $
   ```
   ***
4. Conocer los tipos de datos que se pueden manejar para los atributos en una tabla de MySQL / MariaDB

   A continuación se muestra una lista de los tipos de datos que es posible utilisar con MariaDB, sin embargo es bueno mirar en las páginas oficales de MariaDB o MySQL para consultar si un tipo de dato es soportado y que opciones y restriccione tiene.

   ![Lista de tipos de datos](assets/tipos-de-datos.png)

   __Referencias:__
   1. https://mariadb.com/kb/en/library/data-types/
   2. https://dev.mysql.com/doc/refman/8.0/en/data-types.html
   3. https://disenowebakus.net/tipos-de-datos-mysql.php
   4. https://www.anerbarrena.com/tipos-dato-mysql-5024/

5. Contar con la definición de la tabla o tablas a crear, en este caso la tabla Libro:

   ![Tabla Libro](assets/tabla-libro.jpg)


### DESARROLLO
1. La creación de tablas en SQL se realiza por medio de la instrucción __CREATE TABLE__ y a continuación se muestra la forma de usarla para crear la tabla __Libro__ en la base de datos __Bibllioteca__:

   __Resultado__

   ```bash
   Clase-05/Ejemplo-03 $ docker exec -it pythonsql mysql -hlocalhost -uBiblioteca -p Biblioteca
   Enter password:
   Welcome to the MariaDB monitor.  Commands end with ; or \g.
   Your MariaDB connection id is 13
   Server version: 10.3.15-MariaDB-1:10.3.15+maria~bionic mariadb.org binary distribution

   Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

   Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

   MariaDB [Biblioteca]> CREATE TABLE Libro (id INTEGER PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128), editorial VARCHAR(80), numPag INT, autores INT);
   Query OK, 0 rows affected (0.046 sec)

   MariaDB [Biblioteca]> DESCRIBE Libro;
   +-----------+--------------+------+-----+---------+----------------+
   | Field     | Type         | Null | Key | Default | Extra          |
   +-----------+--------------+------+-----+---------+----------------+
   | id        | int(11)      | NO   | PRI | NULL    | auto_increment |
   | titulo    | varchar(128) | YES  |     | NULL    |                |
   | editorial | varchar(80)  | YES  |     | NULL    |                |
   | numPag    | int(11)      | YES  |     | NULL    |                |
   | autores   | int(11)      | YES  |     | NULL    |                |
   +-----------+--------------+------+-----+---------+----------------+
   5 rows in set (0.001 sec)

   MariaDB [Biblioteca]>
   ```

   __Referencias:__
   1. https://mariadb.com/kb/en/library/create-table
   ***
