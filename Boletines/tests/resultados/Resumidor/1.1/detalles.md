Dentro de los 5 test realizados, el programa ha devuelto un error dentro del test #3 y un fallo en el test #5.
El error encontrado se debe a que la pipeline toma al caracter vacio como un token, siendo que se ingresó como parámetro de max_lenght el valor 0. Se propone como posible solución el asegurarse de pasarle a la API entradas válidas. El fallo en el test #5 demuestra que la API en su estado actual no es capaz de acortar lo suficiente frases repetidas, demostrando que es necesario tener cierta medicion de calidad de artículos entregados para asegurarse de que la información pasada esté bien condicionada. 

| Caso de prueba | Input       | Salida Esperada | Contexto de Ejecución |
| -------------- | ----------- | --------------- | --------------------- |
| #1             | Texto corto | Texto con una cantidad de<br>palabras $\leq$ a la cantidad de<br> palabras del texto original | Se revisa que el programa sea capaz de traducir<br>frases sencillas sin añadir contenido demas |
| #2             | Texto largo | Texto con una cantidad de<br>palabras $\leq$ a la cantidad de<br> palabras del texto original | Se revisa que el programa sea capaz de traducir<br>textos con una gran densidad de contenido <br>que sea capaz de sobrepasar el límite del modelo |
| #3             | Texto vacio | Texto con una cantidad de<br>palabras nula | Se revisa que el programa sea capaz de no añadir<br>contenido demás en entornos vacios en caso de que<br>se entregue erróneamente un dato similar |
| #4             | Texto en inglés | Texto con una cantidad de<br>palabras $\leq$ a la cantidad de<br> palabras del texto original<br>y en el mismo idioma | Se revisa que el programa sea capaz de traducir<br>textos de un idioma que no sea el español |
| #5             | Texto repetido | Texto con una cantidad de<br>palabras considerablemente menor a la cantidad de<br> palabras del texto original | Se revisa que el programa sea capaz de no alargar<br>textos con frases repetitivas |

