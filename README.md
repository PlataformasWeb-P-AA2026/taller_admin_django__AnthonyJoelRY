# taller_admin_django

## Requisitos

Instalar dependencias con el archivo `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

> Si usas el entorno virtual del proyecto:
>
> ```bash
> ./entorno/bin/python -m pip install -r requirements.txt
> ```

## Cómo ejecutar el proyecto Django

1. Activar el entorno virtual (opcional):

```bash
source entorno/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Crear o aplicar migraciones:

```bash
python patrimonio/manage.py makemigrations
python patrimonio/manage.py migrate
```

4. Crear superusuario (opcional):

```bash
python patrimonio/manage.py createsuperuser
```

5. Ejecutar el servidor de desarrollo:

```bash
python patrimonio/manage.py runserver
```

6. Abrir la administración de Django en el navegador:

```
http://127.0.0.1:8000/admin/
```

## Escenarios requeridos

### 1. SQLiteBrowser + Admin de Django

> Espacio reservado para imagen:
>
> ![SQLiteBrowser + Django Admin](./imagenes/sqlite_admin.png)

### 2. PgAdmin + Admin de Django

> Espacio reservado para imagen:
>
> ![PgAdmin + Django Admin](./imagenes/pgadmin_admin.png)

## Configuración de base de datos PostgreSQL

En `patrimonio/patrimonio/settings.py` se puede usar una configuración como:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mi_basedatos',
        'USER': 'mi_usuario',
        'PASSWORD': 'mi_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Git ignore

El proyecto contiene un archivo `.gitignore` que excluye el entorno virtual `entorno/` y archivos comunes de Python/Django.
