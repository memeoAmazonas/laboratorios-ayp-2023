package main

import "fmt"

func main() {
	fmt.Println("Laboratorio 1")
	result := sum(2, 3)
	fmt.Println("El resultado de la suma es", result)
}

func sum(x, y int) int {
	return x + y
}
