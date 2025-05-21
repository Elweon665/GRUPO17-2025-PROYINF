Dentro de los 3 test realizados, el programa ha devuelto que todas las pruebas realizadas respecto a los Pdf fueron un exito, por lo que no existen correcciones
a realizar en este aspecto.

| Caso de prueba | Input       | Salida Esperada | Contexto de Ejecución |
| -------------- | ----------- | --------------- | --------------------- |
| #1             | Descargar Pdf No existente | Devolver el error HTTP<br>404 <br>| Se revisa que el programa de error al tratar de descargar un archivo pdf que no existe |
| #2             | Descargar PDF| El programa detecta la existencia del pdf y lo descarga | Se revisa que el programa busque y encuentre el pdf a descargar, con tal de permitir esta ultima accion |
| #3             | Ver PDF | El programa detecta el pdf y lo muestra en la pagina | Se revisa que el programa sea capaz de encontrar un pdf existente y que pueda mostrarlo al usuario |
