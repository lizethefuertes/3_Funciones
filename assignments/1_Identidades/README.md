![Tec de Monterrey](../../images/logotecmty.png)
# Convertidor a centímetros
**Decisiones - Convierte pies, pulgadas y yardas a centímetros**

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
# Escribe tus funciones abajo de esta línea

def main():
  # Escribe tu código abajo de esta línea
  pass

if __name__ == '__main__':
    main()
```
La línea `#Escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

La función grados_radianes (grados) que recibe una cantidad en grados y regresa su equivalencia en radianes. Utiliza la constante math.pi de la librería math.
.

La función secante_cuadrada (grados) que recibe un ángulo en grados y regresa la secante cuadrada de dicho ángulo. 
secante
Utiliza la función math.tan(x) de la librería math, que calcula la tangente del ángulo x especificado en radianes, por lo tanto, para poder usar esta función, es necesario primero transformar el ángulo en grados a radianes, para ello utiliza la función grados_radianes implementada anteriormente. Como puedes ver, es posible utilizar una función dentro de otra función. La única condición que demanda el compilador, es que la función a utilizar dentro, haya sido definida anteriormente. 

Casos de prueba:

Input: Número de opción (1. Secante)
Input: Ángulo en grados
Output: El resultado de la secante cuadrada

Input: 1
Input: 180
Output: 1.0

Input: 1
Input: 45
Output: 2.0

La función cotangente (grados) que recibe un ángulo en grados y regresa la cotangente de dicho ángulo.  ..
cotangente
Utiliza la función math.tan(x) de la librería math, que calcula la tangente del ángulo x especificado en radianes, por lo tanto para poder usar esta función, es necesario primero transformar el ángulo en grados a radianes como en la función anterior.

Casos de prueba:

Input: Número de opción (2. Cotangente)
Input: Ángulo en grados
Output: El resultado de la cotangente

Input: 2
Input: 45
Output: 1.0

Input: 2
Input: 135
Output: -1.0

La función identidades () que despliegue el siguiente menú en pantalla:
1. Secante cuadrada
2. Cotangente
3. Salir
 
La función main () que utilice la función identidades y de acuerdo a la opción seleccionada por el usuario utilice la función apropiada de las implementadas anteriormente, para calcular la identidad trigonométrica elegida. Utiliza el estatuto de control if anidado. Recuerda que la captura de datos debe ser realizada en la sección del main. Valida opciones incorrectas.
Casos de prueba:

Input: Número de opción (3. Salir o una opción inválida)
Output: Mensaje correspondiente

Input: 3
Output: Adios

Input: 6
Output: ERROR OPCION INVALIDA

Input: -4
Output: ERROR OPCION INVALIDA

En el script principal manda llamar a la función main.

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest` o `pytest --tb=short`,
súbela a tu repositorio en GitHub, con el proceso de `commit + push`.