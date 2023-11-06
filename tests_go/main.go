package main

import (
	"flag"
	"fmt"
	"os"
	"sync"
	"time"
)

func heavyTask(id int) {
	fmt.Printf("Task %d starting\n", id)
	time.Sleep(1 * time.Second)
	fmt.Printf("Task %d completed\n", id)
}

func runConcurrently(numTasks int) {
	var wg sync.WaitGroup
	wg.Add(numTasks)
	fmt.Println("Running concurrently with goroutines...")
	for i := 1; i <= numTasks; i++ {
		go func(id int) {
			defer wg.Done()
			heavyTask(id)
		}(i)
	}
	wg.Wait()
}

func appendToFile(filename, text string) {
	f, err := os.OpenFile(filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()

	if _, err := f.WriteString(text + "\n"); err != nil {
		fmt.Println(err)
	}
}

func main() {
	numTasks := flag.Int("n", 10, "Number of tasks")
	flag.Parse()

	start := time.Now()
	runConcurrently(*numTasks)
	fmt.Printf("Concurrent execution took: %v\n", time.Since(start))
	appendToFile("logs/go.log", fmt.Sprintf("%d,%f", *numTasks, time.Since(start).Seconds()))
}
