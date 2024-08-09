import os
import time
import django   


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from m7_python.models import Inmuebles, Region

def get_list_inmuebles(name, descr):
    lista_inmueble = Inmuebles.objects.filter(nombre_inmueble__icontains=name, descripcion__icontains=descr)


    archi1=open("datos.txt","w")
    for l in lista_inmueble.values():
        archi1.write(str(l))
        archi1.write("\n")

    archi1.close()

    return lista_inmueble


resultado=get_list_inmuebles("Providencia","cocina")
