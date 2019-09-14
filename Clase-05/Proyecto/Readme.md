##### PROYECTO
## BASES DE DATOS EN MYSQL CON PYTHON

### OBJETIVO
Aplicar los conceptos vistos en clase para realizar la operación __CREATE__ para agregar nuevos registros a una tabla desde un script en Python para la base de datos del proyecto BeduTravels.

#### REQUISITOS
1. Contar con los datos de conexión a la base de datos BeduTravels.

   __Host:__ localhost
   __User:__ BeduTravels \
   __Password:__ BeduTravels \
   __Base de datos:__ BeduTravels

1. Contar con la tabla __Usuario__ creada y con datos muestra en la base de datos:

  ![Tabla Usuario](assets/tabla-usuario.jpg)

1. Usar la carpeta de trabajo `Clase-05/Proyecto`

   ```sh
   $ cd Clase-05/Proyecto

   Clase-05/Proyecto $
   ```

### DESARROLLO
1. __OPERACIÓN CREATE__ Crear el script  `agrega-usuario.py` y realizar las modificaciones en el script `modelomysql.py` para que se pueda agregar un nuevo registro a la tabla Usuario en la base de datos BeduTravels desde la línea de comandos. Hacer uso de los módulos `click`, `mysql-connector-python` y `modelomysql`.

   __Caso: Ejecutando el script sin argumentos__

   ```sh
   Clase-05/Proyecto $ python agrega-usuario.py

   Usage: agrega-usuario.py [OPTIONS] NOMBRE APELLIDOS EDAD GENERO
   Try "agrega-usuario.py --help" for help.

   Error: Missing argument "NOMBRE".
   ```

   __Caso: Agregando un registro a la tabla Usuario__

   ```sh
   Clase-05/Proyecto $ python agrega-usuario.py Luis "Mac Rico" 19 M

   Clase-05/Proyecto $ python lista-registros.py Usuario

   Tabla: Usuario
   --------------
   Id | Nombre | Apellidos | Edad | Genero
    1 | Hugo   | Mac Rico  |   10 | M     
    2 | Paco   | Mac Rico  |   15 | M     
    3 | Daisy  | Mac Rico  |   18 | H     
    4 | Luis   | Mac Rico  |   19 | M     
   --------------
   ```
   ***

__Nota:__ Este reto se realiza en 15 mins.
