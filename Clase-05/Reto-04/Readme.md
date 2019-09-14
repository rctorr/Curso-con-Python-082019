##### RETO-04
## CRUD DE DATOS EN MARIADB

### OBJETIVO
Hacer uso de las instrucciones para realizar un CRUD de datos a una tabla en MariaDB

#### REQUISITOS
1. Contar con la base de datos BeduTravels inicializada y con los datos de conexión:

   __Host:__ localhost \
   __User:__ BeduTravels \
   __Password:__ BeduTravels \
   __Base de datos:__ BeduTravels

1. Contar con la tabla __Usuario__ creada en la base de datos:

   ![Tabla Usuario](assets/tabla-usuario.jpg)

1. Abrir una terminal o consola de comandos y cambiarse a la carpeta de trabajo `Clase-05/Reto-04`

   ```sh
   $ cd Clase-05/Reto-04

   Clase-05/Reto-04 $ tree
   .
   ├── assets
   │   └── tabla-usuario.jpg
   ├── Readme.md
   └── sql
       ├── bedutravels.sql
       └── tabla-usuario.sql

   Clase-05/Reto-04 $
   ```
   ***


### DESARROLLO
1. Se realiza las operaciones necesarias para agregar la siguiente lista de personas a la tabla __Usuario__.

   | Nombre | Apellidos | Edad | Género |
   | ------ | --------- | ---- | ------ |
   | Hugo | Mac Rico | 10 | M |
   | Paco | Mac Pobre | 15 | M |
   | Daisy | Mac Rico | 18 | H |
   | Pluto | Mac Rico | 8 | M |

   __Resultado__

   ```sql
   MariaDB [BeduTravels]> INSERT INTO Usuario VALUES (null, "Hugo", "Mac Rico", 10, "M");
   Query OK, 1 row affected (0.001 sec)

   MariaDB [BeduTravels]> INSERT INTO Usuario VALUES (null, "Paco", "Mac Pobre", 15, "M");
   Query OK, 1 row affected (0.001 sec)

   MariaDB [BeduTravels]> INSERT INTO Usuario VALUES (null, "Daisy", "Mac Rico", 18, "H");
   Query OK, 1 row affected (0.001 sec)

   MariaDB [BeduTravels]> INSERT INTO Usuario VALUES (null, "Pluto", "Mac Rico", 8, "M");
   Query OK, 1 row affected (0.001 sec)

   MariaDB [BeduTravels]> SELECT * FROM Usuario;
   +----+--------+-----------+------+--------+
   | id | nombre | apellidos | edad | genero |
   +----+--------+-----------+------+--------+
   |  1 | Hugo   | Mac Rico  |   10 | M      |
   |  2 | Paco   | Mac Pobre |   15 | M      |
   |  3 | Daisy  | Mac Rico  |   18 | H      |
   |  4 | Pluto  | Mac Rico  |    8 | M      |
   +----+--------+-----------+------+--------+
   4 rows in set (0.000 sec)

   MariaDB [BeduTravels]>
   ```
   ***


2. Realizar las operaciones necesarias para que la tabla de __Usuario__ contenga los siguientes registros:

   __Resultado__

   ```sql
   MariaDB [BeduTravels]> UPDATE Usuario SET apellidos="Mac Rico" WHERE id=2;Query OK, 1 row affected (0.001 sec)
   Rows matched: 1  Changed: 1  Warnings: 0

   MariaDB [BeduTravels]> DELETE FROM Usuario WHERE id=4;
   Query OK, 1 row affected (0.001 sec)

   MariaDB [BeduTravels]> SELECT * FROM Usuario;
   +----+--------+-----------+------+--------+
   | id | nombre | apellidos | edad | genero |
   +----+--------+-----------+------+--------+
   |  1 | Hugo   | Mac Rico  |   10 | M      |
   |  2 | Paco   | Mac Rico  |   15 | M      |
   |  3 | Daisy  | Mac Rico  |   18 | H      |
   +----+--------+-----------+------+--------+
   3 rows in set (0.000 sec)

   MariaDB [BeduTravels]>
   ```
   ***
