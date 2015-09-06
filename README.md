#Aplicacion Blog

#Login admin en /admin:
Usuario: ubuntu

Password: tenita  

#Modelo
Modelo Blog:

    - Autor
    - Titulo
    - Cuerpo de texto
    - Fecha Creacion -> Se asigna con la hora del sistema cuando se añade la entrada a la base de datos de entradas
    - Fecha Publicacion -> Se asigna con la hora del sistema cuando se llama a la funcion publica

#Funcionalidad
La url " /  " nos lleva a lista_entradas.html que muestra todas las entradas guardadas en la base de datos.

Para que una entrada pase a estar en la lista_entradas hay que llamar a su metodo publica() via shell de django.
Una vez en el shell hacer "from blogs.models import Entrada"
Obtener la entrada que queramos de "Entrada.objects" y hacer la llamada a publica()

Si se crea una entrada desde el formulario web, al hacer click en el boton submit se tramita la peticion post,
creandose la entrada del blog y publicandose a la vez (Sin necesidad alguna de django shell)

Solo estando logado en el blog se pueden crear o editar entradas.
Si se edita una entrada al tener un funcionamiento similar al formulario de creacion (basicamente el mismo) la hora de publicacion
de la entrada pasa a ser la de cuando se ejecutó la edición, aunque estuviese publicada previamente la entrada.

Tanto al crear como editar una entrada via formulario web, al ejecutarse la accián post se nos redigirá a la entrada que hemos creado/modificado.
