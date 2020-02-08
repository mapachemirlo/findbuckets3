# Findbuckets3
Findbuckets3 es un pequeño script para buscar buckets s3 utilizando el buscador grayhatwarfare, actualmente está en etapada de desarrollo, la idea es agregarle más funcionalidad.

# Requisitos
Python 3.*

# Instalación
Clone el repositorio a su directorio local:

`https://github.com/mapachemirlo/findbuckets3.git`

Instale las dependencias:

`pip install -r requirements.txt`

Si tiene inconvenientes con mechanize, pruebe instalando por separado:

`pip install -U mechanize` o descargando el archivo desde http://wwwsearch.sourceforge.net/mechanize/src/ y ejecutando `setup.py`.

Puede agregar el archivo `findbuckets3.py` al $PATH para más comodidad.

# Uso
Ejecute:

`python findbuckets3.py -b palabra`

# Nota
Tal vez deba agregar utf-8 de la siguiente manera:
`export PYTHONIOENCODING=UTF-8`
