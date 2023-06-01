package main

import "fmt"

func main() {
	fmt.Println("Laboratorio 1")

	result := sum(2, 3)
	fmt.Println("El resultado de la suma es", result)
	resultWithMe := dependWithMe(2, 3)
	fmt.Println("El resultado es: ", resultWithMe)
}

func sum(x, y int) int {
	return x + y
}

func dependWithMe(x, y int) int {
	if x > y {
		return x * y
	}
	if x < y {
		return (x * y) - (x + y)
	}
	return (x * y) * 2
}
