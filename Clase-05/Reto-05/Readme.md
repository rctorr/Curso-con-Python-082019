##### RETO-05
## CRUD DE DATOS CON PYTHON EN MYSQL

### OBJETIVO
Aplicar el procedimiento para realizar un CRUD de datos a una tabla en un servidor MariaDB desde Python a una base de datos y tabla diferentes.

#### REQUISITOS
1. Contar con los datos de conexión a la base de datos BeduTravels.

   __Host:__ localhost
   __User:__ BeduTravels \
   __Password:__ BeduTravels \
   __Base de datos:__ BeduTravels

1. Contar con la tabla __Usuario__ creada y con datos muestra en la base de datos:

  ![Tabla Usuario](assets/tabla-usuario.jpg)

1. Usar la carpeta de trabajo `Clase-05/Reto-05`

   ```sh
   $ cd Clase-05/Reto-05

   Clase-05/Reto-05 $
   ```

### DESARROLLO
1. __OPERACIÓN READ__ Realizar las modificaciones necesarias en los scripts `lista-registros.py` y `modelomysql.py` para que se imprima en formato texto en la salida estándar la lista de registros de la tabla proporcionada de la base de datos BeduTravels.

   __Caso: Ejecutando el script sin argumentos__

   ```sh
   Clase-05/Reto-05 $ python lista-registros.py

   Tablas disponibles
   ------------------
   Usuario
   ------------------
   ```

   __Caso: Imprimiendo registros de la tabla Usuario__

   ```sh
   Clase-05/Reto-05 $ python lista-registros.py Usuario

   Tabla: Usuario
   --------------
   Id | Nombre | Apellidos | Edad | Genero
    1 | Hugo   | Mac Rico  |   10 | M     
    2 | Paco   | Mac Rico  |   15 | M     
    3 | Daisy  | Mac Rico  |   18 | H     
   --------------
   ```
   ***

__Nota:__ Este reto se realiza en 3 mins o menos.
