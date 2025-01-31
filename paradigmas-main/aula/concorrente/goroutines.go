package main

import (
	"fmt"
	"time"
)

func trabalho(nome string) {
	fmt.Println(nome, "iniciou")
	time.Sleep(2 * time.Second)
	fmt.Println(nome, "finalizou")
}

func main() {
	go trabalho("Goroutine 1")
	go trabalho("Goroutine 2")
	go trabalho("Goroutine 3")
	go trabalho("Goroutine 4")
	go trabalho("Goroutine 5")
	go trabalho("Goroutine 6")

	time.Sleep(3 * time.Second)
	fmt.Println("todos trabalhos foram finalizados")
}