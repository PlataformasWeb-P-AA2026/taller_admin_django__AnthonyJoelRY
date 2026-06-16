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
<img width="1600" height="1000" alt="image" src="https://github.com/user-attachments/assets/3e479c6a-f8f0-4a9d-9efc-4e6482aa9fa2" />

### 2. PgAdmin + Admin de Django
<img width="1600" height="1000" alt="image" src="https://github.com/user-attachments/assets/8bbcfd73-3f57-4585-8fc2-f6559452439c" />


## Git ignore

El proyecto contiene un archivo `.gitignore` que excluye el entorno virtual `entorno/` y archivos comunes de Python/Django.
