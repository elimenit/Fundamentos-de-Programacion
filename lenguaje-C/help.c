#include <stdio.h> //biblioteca estandar
#include <stdbool.h> // para los booleanos
#include <stdlib.h> //para gestion de la memoria malloc realloc calloc
/*
Cada instruccion el programa debe saber todo(tipo de dato), valor de retorno
los parecentesis le indican que hasta es el alcanze de una funcion o bucle
Sintaxis parecida a la de Java
usamos for cuando sabemos cuantas veces iterar
While si no sabemos cuantas veces iterar y hay una condicion
seguimos el paradigma pe la programacion estructurada y modular (primero se declaran las variables
 y despues lo separamos en funciones reutilizables)
una funcion solo hace una cosa y bien
*/
// valor de retorno de la funcion 
int funcion(int numero ) {
    // inicio; condicion; control
    for (numero; numero > 10; numero--) {
        printf("%d ", numero); // usamos formateadores para poder mostrar un numero a acceder a ella
    } 
    printf("\n"); // Hacemos un salto de linea (Alt Gr+ ?)
    return numero;
}
void loop_infinity() {
    while(true) {
        printf("Estas en un bucle infinito");

    }
}
void punteros () {
    printf("Este es el tema mas importante\n");
    // implementalo tu puedes accede a la direccion 0x000000
    // si logras considerate genio
}
int ingreso_usuario() {
    int numero = 10;
    int scanner;
    do {
        printf("Ingresa un numero:\n");
        // le indicamos el tipo de variable y en que direccion de memoria se almacena
        scanf("%d", &scanner); 
    } while( scanner > numero);
    while (numero > 0) {
        printf("Ingresastes este numero :%d \n");
        numero --; //restamos en uno
    }
    
}
// en cada programa que realizes siempre tiene que haber al menos una funcion main
// si no tu programa que desarrollas no tiene funcion main no es funcional y si 
// lo es demuestralo
int main() {   
    printf("Hola Mundo");  // termina en ; no negociable
    return 0; // <- Si o si tiene que ir no negociable
}