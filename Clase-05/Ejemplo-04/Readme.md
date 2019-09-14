##### EJEMPLO-04
## CRUD DE DATOS EN MARIADB

### OBJETIVO
Conocer las instrucciones para realizar un CRUD de datos a una tabla en MariaDB

#### REQUISITOS
1. Contar con la base de datos Biblioteca inicializada y con los datos de conexión:

   __Host:__ localhost \
   __User:__ Biblioteca \
   __Password:__ Biblioteca \
   __Base de datos:__ Biblioteca

1. Contar con la tabla __Libro__ creada en la base de datos:

  ![Tabla Libro](assets/tabla-libro.jpg)

1. Abrir una terminal o consola de comandos y cambiarse a la carpeta de trabajo `Clase-05/Ejemplo-04`

   ```sh
   $ cd Clase-05/Ejemplo-04

   Clase-05/Ejemplo-04 $ ls
   Readme.md

   Clase-05/Ejemplo-04 $
   ```
   ***

1. Conocer el concepto de CRUD de datos que se descripbe a continuación:

   - __C__reate Operación que permite crear o insertar nuevos registros a una tabla.
   - __R__read  Operación que permite la lectura o consulta de registros o datos en una tabla.
   - __U__pdate Operación que permite la actualización de registros en una tabla.
   - __D__elete Operación que permite la eliminación de registros en una tabla.

### DESARROLLO
1. __OPERACIÓN READ__ Se realiza normalmente con la instrucción __SELECT__ de SQL y la forma de consultar todos los registros disponibles en la tabla Libro es la siguiente:

   __Resultado__

   ```bash
   MariaDB [Biblioteca]> SELECT * FROM Libro;
   Empty set (0.000 sec)

   MariaDB [Biblioteca]>
   ```
   Observar que la lista de registros está vacía.

   __Referencias:__
   1. https://mariadb.com/kb/en/library/select
   ***


2. __OPERACIÓN CREATE__ Se realiza normalmente con la instrucción __INSERT INTO__ de SQL a continuación se muestra como agregar la siguiente lista de libros a la tabla __Libro__.

   | Título | Editorial | Núm. de págs. | Autores |
   | ------ | --------- | ------------- | ------- |
   | Yo, Robot | Genome Press | 374 | 1 |
   | El fin de la eternidad | Gnome Press | 191 | 1 |
   | El arte de la gerra | Obelisco | 112 | 2 |

   __Resultado__

   ```sql
   MariaDB [Biblioteca]> INSERT INTO Libro VALUES (null, "Yo, Robot", "Gnome Press", 374, 1);
   Query OK, 1 row affected (0.006 sec)

   MariaDB [Biblioteca]> INSERT INTO Libro VALUES (null, "El fin de la eternidad", "Gnome Press", 191, 1);
   Query OK, 1 row affected (0.001 sec)

   MariaDB [Biblioteca]> INSERT INTO Libro VALUES (null, "El arte de la guerra", "Obelisco", 112, 2);
   Query OK, 1 row affected (0.001 sec)

   MariaDB [Biblioteca]> SELECT * FROM Libro;
   +----+------------------------+-------------+--------+---------+
   | id | titulo                 | editorial   | numPag | autores |
   +----+------------------------+-------------+--------+---------+
   |  1 | Yo, Robot              | Gnome Press |    374 |       1 |
   |  2 | El fin de la eternidad | Gnome Press |    191 |       1 |
   |  3 | El arte de la gerra    | Obelisco    |    112 |       2 |
   +----+------------------------+-------------+--------+---------+
   3 rows in set (0.000 sec)

   MariaDB [Biblioteca]>

   ```

   __Referencias:__
   1. https://sqlite.org/lang_insert.html
   ***


3. __OPERACIÓN UPDATE__ Se realiza normalmente con la instrucción __UPDATE__ de SQL y a continuación se muestra como corregir el nombre del libro "El arte de la gerra" por "El arte de la guerra".

   __Resultado__

   ```sql
   MariaDB [Biblioteca]> SELECT * FROM Libro;
   +----+------------------------+-------------+--------+---------+
   | id | titulo                 | editorial   | numPag | autores |
   +----+------------------------+-------------+--------+---------+
   |  1 | Yo, Robot              | Gnome Press |    374 |       1 |
   |  2 | El fin de la eternidad | Gnome Press |    191 |       1 |
   |  3 | El arte de la gerra    | Obelisco    |    112 |       2 |
   +----+------------------------+-------------+--------+---------+
   3 rows in set (0.000 sec)

   MariaDB [Biblioteca]> UPDATE Libro SET titulo="El arte de la guerra" WHERE id=3;
   Query OK, 0 rows affected (0.000 sec)
   Rows matched: 1  Changed: 0  Warnings: 0

   MariaDB [Biblioteca]> SELECT * FROM Libro;+----+------------------------+-------------+--------+---------+
   | id | titulo                 | editorial   | numPag | autores |
   +----+------------------------+-------------+--------+---------+
   |  1 | Yo, Robot              | Gnome Press |    374 |       1 |
   |  2 | El fin de la eternidad | Gnome Press |    191 |       1 |
   |  3 | El arte de la guerra   | Obelisco    |    112 |       2 |
   +----+------------------------+-------------+--------+---------+
   3 rows in set (0.000 sec)

   MariaDB [Biblioteca]>
   ```

   __Referencias:__
   1. https://mariadb.com/kb/en/library/update
   ***


3. __OPERACIÓN DELETE__ Se realiza normalmente con la instrucción __DELETE__ de SQL y a continuación se muestra como agrega un registro erroneo y luego se elimina:

   __Resultado__

   ```sql

   MariaDB [Biblioteca]> INSERT INTO Libro VALUES (null, "Don Quijote de la Mancha", "Desconocida", 863, 3);
   Query OK, 1 row affected (0.001 sec)

   MariaDB [Biblioteca]> SELECT * FROM Libro;+----+--------------------------+-------------+--------+---------+
   | id | titulo                   | editorial   | numPag | autores |
   +----+--------------------------+-------------+--------+---------+
   |  1 | Yo, Robot                | Gnome Press |    374 |       1 |
   |  2 | El fin de la eternidad   | Gnome Press |    191 |       1 |
   |  3 | El arte de la guerra     | Obelisco    |    112 |       2 |
   |  4 | Don Quijote de la Mancha | Desconocida |    863 |       3 |
   +----+--------------------------+-------------+--------+---------+
   4 rows in set (0.000 sec)

   MariaDB [Biblioteca]> DELETE FROM Libro WHERE id=4;
   Query OK, 1 row affected (0.001 sec)

   MariaDB [Biblioteca]> SELECT * FROM Libro;+----+------------------------+-------------+--------+---------+
   | id | titulo                 | editorial   | numPag | autores |
   +----+------------------------+-------------+--------+---------+
   |  1 | Yo, Robot              | Gnome Press |    374 |       1 |
   |  2 | El fin de la eternidad | Gnome Press |    191 |       1 |
   |  3 | El arte de la guerra   | Obelisco    |    112 |       2 |
   +----+------------------------+-------------+--------+---------+
   3 rows in set (0.000 sec)

   MariaDB [Biblioteca]>
   ```

   __Referencias:__
   1. https://mariadb.com/kb/en/library/delete
   ***
