// inventory.go

package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Item struct {
	Name     string
	Price    float64
	Quantity int
}

func totalValue(items []Item) float64 {
	total := 0.0
	for _, item := range items {
		total += item.Price * float64(item.Quantity)
	}
	return total
}

func main() {
	rand.Seed(time.Now().UnixNano())

	items := []Item{
		{"Laptop", 999.99, rand.Intn(5) + 1},
		{"Keyboard", 79.99, rand.Intn(20) + 1},
		{"Mouse", 39.99, rand.Intn(25) + 1},
		{"Monitor", 249.99, rand.Intn(10) + 1},
		{"Webcam", 59.99, rand.Intn(15) + 1},
	}

	fmt.Println("=== Inventory Report ===")

	for _, item := range items {
		fmt.Printf(
			"%-10s Qty: %2d Price: $%6.2f\n",
			item.Name,
			item.Quantity,
			item.Price,
		)
	}

	fmt.Printf("\nTotal Inventory Value: $%.2f\n", totalValue(items))
}
