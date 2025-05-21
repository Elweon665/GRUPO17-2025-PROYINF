Dentro de los 5 test realizados, el programa ha devuelto errores dentro del código del programa en los casos #2 y #5.
Después de estudiar más a fondo la lógica del programa, se ha encontrado un error en donde se podian pasar chunks con una cantidad
de tokens mayor al que puede soportar la pipeline. Este problema ha sido corregido en la versión 1.1 (actualmente implementada)

| Caso de prueba | Input       | Salida Esperada | Contexto de Ejecución |
| -------------- | ----------- | --------------- | --------------------- |
| #1             | Texto corto | Texto con una cantidad de<br>palabras $\leq$ a la cantidad de<br> palabras del texto original | Se revisa que el programa sea capaz de traducir<br>frases sencillas sin añadir contenido demas |
| #2             | Texto largo | Texto con una cantidad de<br>palabras $\leq$ a la cantidad de<br> palabras del texto original | Se revisa que el programa sea capaz de traducir<br>textos con una gran densidad de contenido <br>que sea capaz de sobrepasar el límite del modelo |
| #3             | Texto vacio | Texto con una cantidad de<br>palabras nula | Se revisa que el programa sea capaz de no añadir<br>contenido demás en entornos vacios en caso de que<br>se entregue erróneamente un dato similar |
| #4             | Texto en inglés | Texto con una cantidad de<br>palabras $\leq$ a la cantidad de<br> palabras del texto original<br>y en el mismo idioma | Se revisa que el programa sea capaz de traducir<br>textos de un idioma que no sea el español |
| #5             | Texto repetido | Texto con una cantidad de<br>palabras $\leq$ a la cantidad de<br> palabras del texto original | Se revisa que el programa sea capaz de no alargar<br>textos con frases repetitivas |

