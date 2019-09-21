`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 06`](../Readme.md) > Reto-04
## Consulta de datos en una relación muchos a muchos con SQL

### OBJETIVO
Realizar una consulta de datos a dos o más tablas para el proyecto BeduTravels.

#### REQUISITOS
1. Modelo de entidad-relación:

   ![Diagrama entidad-relación](modelo-entidad-relacion.jpg)

1. Carpeta de repo actualizada
1. Usar la carpeta de trabajo `Clase-06/Reto-04`


#### DESARROLLO
1. Mostrar la lista de todas las reservas realizadas incluyendo el nombre del origen, destino, fecha de salida, fecha de regreso y nombre de usuario.

   __Conectándose a la base de datos:__

    ```bash
    Clase-06/Reto-04 $ docker exec -it -e LANG=C.UTF-8 mariadb mysql -hlocalhost -uBeduTravels -pBeduTravels BeduTravels
    [...]
    MariaDB [BeduTravels]>
    ```

   __Realizando la consulta haciendo uso del mítico JOIN:__

   ```sql
   SELECT Lugar.nombre, Destino.nombre, fechaSalida, fechaRegreso, Usuario.nombre FROM Reserva JOIN Usuario ON Usuario.id=idUsuario JOIN Viaje ON idViaje=Viaje.id JOIN Lugar ON idOrigen=Lugar.id JOIN Lugar as Destino ON idDestino=Destino.id;
   +--------+-------------+-------------+--------------+--------+
   | nombre | nombre      | fechaSalida | fechaRegreso | nombre |
   +--------+-------------+-------------+--------------+--------+
   | CDMX   | Guadalajara | 2019-06-05  | 2019-06-12   | Daisy  |
   +--------+-------------+-------------+--------------+--------+
   1 row in set (0.000 sec)
   ```
