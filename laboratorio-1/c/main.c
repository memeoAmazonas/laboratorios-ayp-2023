#include <stdio.h>
#include <math.h>
// gcc main.c -o main
// ./main

int sum(int x, int y);

int main() {
   printf("Laboratorio 1\n");
   int resultSum;
   resultSum = sum(3,3);
   printf("El resultado de la suma 2 es: %d\n",resultSum);
   return 0;
}

int sum(int x, int y){
return x+ y;
}