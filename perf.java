class perf {

    public static void main(String[] args) throws InterruptedException {


        final int count = Integer.parseInt(args[0]);
        final int n = Integer.parseInt(args[1]);
        System.out.println("counting " + count + " using " + n + " threads.");

        Thread[] rr = new Thread[n];
        for(int i=0;i<n;i++){
            Thread r = new Thread() {
                @Override
                public void run() {
                    count_down(count/n);
                }
            };
            rr[i] = r;
        }

        long start = System.nanoTime();

        for(Thread r : rr) r.start();
        for(Thread r : rr) r.join();

        long end = System.nanoTime();

        float elapsed = end - start;
        elapsed /= 1e9;

        System.out.println(elapsed + " sec");

    }

    public static void count_down(int count){
        while(count>0) count--;
    }

}

//cwmbp:eval_thread $ javac perf.java -d . && java perf 1000000 1
//counting 1000000 using 1 threads.
//0.001787497 sec
//cwmbp:eval_thread $ javac perf.java -d . && java perf 1000000 2
//counting 1000000 using 2 threads.
//0.003153525 sec
//cwmbp:eval_thread $ javac perf.java -d . && java perf 1000000 3
//counting 1000000 using 3 threads.
//0.006721287 sec
//cwmbp:eval_thread $ javac perf.java -d . && java perf 1000000 4
//counting 1000000 using 4 threads.
//0.013412097 sec
//cwmbp:eval_thread $ javac perf.java -d . && java perf 1000000 5
//counting 1000000 using 5 threads.
//0.011507518 sec
//cwmbp:eval_thread $ javac perf.java -d . && java perf 1000000 6
//counting 1000000 using 6 threads.
//0.010349789 sec
