package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()
	c := make(chan interface{})
	//var c <-chan int
	go func() {
		time.Sleep(5 * time.Second)
		close(c) // <1>
	}()

	fmt.Println("Blocking on read...")
	select {
	/*
		//if no data, then block,but if there is the default, the default will run and exit
		//and the chan is null, then blocking to deadlock
	 */

	case <-c: // <2>
		fmt.Printf("Unblocked %v later.\n", time.Since(start))
	//default:
	}
}
