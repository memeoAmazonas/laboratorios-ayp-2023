#include <stdio.h>
#include <math.h>
// gcc main.c -o main
// ./main

int sum(int x, int y);
int dependWithMe(int x, int y);


int main() {
   printf("Laboratorio 1\n");
   int resultSum;
   int resultWithMe;
   resultSum = sum(3,3);
   resultWithMe = dependWithMe(1,2);
   printf("El resultado de la suma 2 es: %d\n",resultWithMe);

   return 0;
}

int sum(int x, int y){
return x+ y;
}
int dependWithMe(int x, int y){
    if (x > y) return x * y;
    if (x < y) return (x * y)-(x + y);
    return (x * y)*2;
}