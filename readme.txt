(si está en ubuntu)

Primero, abra una terminal en la carpeta del repositorio y cree el entorno (esto generará la carpeta env localmente)

python3 -m venv env

luego, en la terminal del repositorio ejecute

source env/bin/activate

este código activará el entorno, después, deberá instalar las dependencias y posteriormente abrir los programas

pip install -r requisitos.txt  #dependencias

comandos para ejecutar los programas:

python3 RegresionPoisson.py #por ejemplo
python3 Bikers.py
python3 clasicModelOSL.py
