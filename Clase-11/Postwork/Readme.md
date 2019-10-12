`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 11`](../Readme.md) > Postwork
## Aplicar los conceptos de la clase a tú Postwork.

### OBJETIVO
- Instalar Django Rest Framework
- Configurar Django Rest Framework
- Definir las urls para los modelos que se necesiten acceder por medio del __API__.
- Integrar Django Rest Framework en tú proyecto
- Realizar operaciones de CRUD vía API

### REQUISITOS
1. Actualizar repositorio
1. Usar la carpeta de trabajo `Clase-11/Postwork`
1. Contar con tú Proyecto ya en Django ya con los modelos (tablas) a usar definidos, así como sus relaciones.

### DESARROLLO
1. Instalar Django Rest Framework

   __Actualizar archivo `requeriments.txt` para incluir el módulo instalado__

   __Nota:__ Recuerda incluir el archivo `requeriments.txt` en tu repo para que ya sea tú o tú equipo pueda replicar el entorno de desarrollo y además sea homogénelo.

1. Agregar Django Rest Framework a la configuración en el archivo `settings.py` como una aplicación adicional:

1. Crear la ruta para la url `/api/mitabla` modificando el archivo `Proyecto/myapp/urls.py`:

1. Crear la vista para el api de la tabla __MiTabla__ aunque en este caso en lugar de generar y regresar HTML será JSON.

   __Abrir el archivo `Proyecto/myapp/views.py` y agregar la vista definida en urls.py__

1. Crear el serializador `MiTablaSerializer` en el archivo `Proyecto/myapp/serializers.py`.

1. Acceder y verificar el funcioamiento de la __API__  en `/api/mitabla`

   __Para tener acceso al API abrir la siguiente url:__

   http://localhost:8000/api/mitabla/

Realizar el proceso anterior por cada modelo o tabla que se requiera acceder desde el __API__.
