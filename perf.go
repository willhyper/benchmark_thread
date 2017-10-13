package main

import(
	"fmt"
	"time"
	"os"
	"strconv"
	"sync"
)

func main() {

	count, _ := strconv.Atoi(os.Args[1])
	n, _ := strconv.Atoi(os.Args[2])
	fmt.Println("counting", count, "using", n, "goroutines.")

	wg := sync.WaitGroup{}
	wg.Add(n)

	start := time.Now().Nanosecond()

	for i:=0;i<n;i++ {
		go count_down(&wg, count/n)
	}

	wg.Wait()
	end := time.Now().Nanosecond()

	elapse := float64(end-start)/1e9

	fmt.Println(elapse, "sec")

}

func count_down(wg *sync.WaitGroup, count int){
	defer wg.Done()
	for c:= count; c>0; c--{
	}
}

//cwmbp:eval_thread $ go run perf.go 1000000 1
//counting 1000000 using 1 goroutines.
//0.000393292 sec
//cwmbp:eval_thread $ go run perf.go 1000000 2
//counting 1000000 using 2 goroutines.
//0.000324649 sec
//cwmbp:eval_thread $ go run perf.go 1000000 3
//counting 1000000 using 3 goroutines.
//0.000235673 sec
//cwmbp:eval_thread $ go run perf.go 1000000 4
//counting 1000000 using 4 goroutines.
//0.000241832 sec
//cwmbp:eval_thread $ go run perf.go 1000000 5
//counting 1000000 using 5 goroutines.
//0.000311839 sec
//cwmbp:eval_thread $ go run perf.go 1000000 6
//counting 1000000 using 6 goroutines.
//0.000311991 sec
//cwmbp:eval_thread $ go run perf.go 1000000 7
//counting 1000000 using 7 goroutines.
//0.000226289 sec
