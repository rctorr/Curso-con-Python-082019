`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 06`](../Readme.md) > Ejemplo-04
## Consulta de datos en una relación muchos a muchos con SQL

### OBJETIVO
Conocer la forma recomendada para realizar una consulta de datos a dos o más tablas.

#### REQUISITOS
1. Modelo de entidad-relación:

   ![Diagrama entidad-relación](modelo-entidad-relacion.jpg)

1. Carpeta de repo actualizada
1. Usar la carpeta de trabajo `Clase-06/Ejemplo-04`


#### DESARROLLO
1. Mostrar la lista de todos los préstamos realizados incluyendo además el nombre del usuario en lugar del idUsuario.

   __Conectándose a la base de datos:__

    ```bash
    Clase-06/Ejemplo-04 $ docker exec -it -e LANG=C.UTF-8 mariadb mysql -hlocalhost -uBiblioteca -pBiblioteca Biblioteca
    [...]
    MariaDB [Biblioteca]>
    ```

    __La lista de todos los préstamos se obtiene de la siguiente forma:__

    ```sql
    SELECT * FROM Prestamo;
    +----+-----------+------------+----------+
    | id | idUsuario | fechaPre   | fechaDev |
    +----+-----------+------------+----------+
    |  1 |         1 | 2019-06-05 | NULL     |
    +----+-----------+------------+----------+
    1 row in set (0.000 sec)
    ```
    Pero esto no proporciona el nombre del usuario, así que para obtener este resultado hay que hacer uso de la relación con la tabla Usuario por medio de la instrucción SQL JOIN.

   __Realizando la consulta haciendo uso del mítico JOIN, intento 1:__

   ```sql
   SELECT * FROM Prestamo JOIN Usuario;
   +----+-----------+------------+----------+----+---------+-----------+------+--------+---------------------------------+
   | id | idUsuario | fechaPre   | fechaDev | id | nombre  | apellidos | edad | genero | direccion                       |
   +----+-----------+------------+----------+----+---------+-----------+------+--------+---------------------------------+
   |  1 |         1 | 2019-06-05 | NULL     |  1 | Ricardo | Torres    |   46 | H      | Unidad de los Patos, Candelaria |
   |  1 |         1 | 2019-06-05 | NULL     |  2 | Tony    | Stark     |   45 | H      | Stark Tower                     |
   |  1 |         1 | 2019-06-05 | NULL     |  3 | Black   | Widow     |   30 | M      | Unidad de los Patos, Candelaria |
   |  1 |         1 | 2019-06-05 | NULL     |  4 | Cap     | America   |  200 | H      | Desconocida                     |
   +----+-----------+------------+----------+----+---------+-----------+------+--------+---------------------------------+
   4 rows in set (0.000 sec)
   ```
   Observar que el resultado ha relacionado el único registro de la tabla __Prestamo__ con todos los registros de la tabla __Usuario__, a esto se le conoce como el producto cruz entre tablas.

   __NOTA:__ Este esta es una de las peores consultas que se pueden realizar, ya que si por ejemplo ambas tablas tubieran unos 100 mil registros la cantidad de regristros generado en la consulta sería de 100000 x 100000 = 10 000 000 000 de registros, si las tablas tubieran 1 millón de registros la cantidad de información regresada podría ser de Terabytes o Pentabytes de información.

   __ADVERTENCIA:__ __HAY TABLA__ [Ver diapos]

   __Realizando la consulta haciendo uso del mítico JOIN, intento 2:__

   ```sql
   SELECT * FROM Prestamo JOIN Usuario ON Prestamo.idUsuario=Usuario.id;
   +----+-----------+------------+----------+----+---------+-----------+------+--------+---------------------------------+
   | id | idUsuario | fechaPre   | fechaDev | id | nombre  | apellidos | edad | genero | direccion                       |
   +----+-----------+------------+----------+----+---------+-----------+------+--------+---------------------------------+
   |  1 |         1 | 2019-06-05 | NULL     |  1 | Ricardo | Torres    |   46 | H      | Unidad de los Patos, Candelaria |
   +----+-----------+------------+----------+----+---------+-----------+------+--------+---------------------------------+
   1 row in set (0.000 sec)
   ```
   El resultado se reduce exponencialmente, pero aún tenemos datos adicionales, así que se procede a elegir sólo los necesarios.

   __Realizando la consulta haciendo uso del mítico JOIN, intento 3:__

   ```sql
   SELECT Prestamo.id, nombre, fechaPre, fechaDev FROM Prestamo JOIN Usuario ON Prestamo.idUsuario=Usuario.id;
   +----+---------+------------+----------+
   | id | nombre  | fechaPre   | fechaDev |
   +----+---------+------------+----------+
   |  1 | Ricardo | 2019-06-05 | NULL     |
   +----+---------+------------+----------+
   1 row in set (0.000 sec)
   ```
   Este es el resultado esperado.
   ***

1. Mostrar la lista de todos los libros prestados incluyendo el título del libro, la fecha de préstamo y el nombre de a quien se ha prestado.

   __Realizando la consulta haciendo uso del mítico JOIN, en un intento:__

   ```sql
   SELECT titulo, fechaPre, nombre FROM LibroPrestamo JOIN Libro ON LibroPrestamo.idLibro=Libro.id JOIN Prestamo ON LibroPrestamo.idPrestamo=Prestamo.id JOIN Usuario ON Prestamo.idUsuario=Usuario.id;
   +------------------------+------------+---------+
   | titulo                 | fechaPre   | nombre  |
   +------------------------+------------+---------+
   | Yo, Robot              | 2019-06-05 | Ricardo |
   | El fin de la eternidad | 2019-06-05 | Ricardo |
   +------------------------+------------+---------+
   2 rows in set (0.000 sec)
   ```
