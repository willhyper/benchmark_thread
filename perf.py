#
# cwmbp:eval_thread $ python perf.py 1000000 1
# counting 1000000 using 1 threads.
# 0.08722496032714844 sec
# cwmbp:eval_thread $ python perf.py 1000000 2
# counting 1000000 using 2 threads.
# 0.0799858570098877 sec
# cwmbp:eval_thread $ python perf.py 1000000 3
# counting 1000000 using 3 threads.
# 0.07736515998840332 sec
# cwmbp:eval_thread $ python perf.py 1000000 4
# counting 1000000 using 4 threads.
# 0.07988691329956055 sec
# cwmbp:eval_thread $ python perf.py 1000000 5
# counting 1000000 using 5 threads.
# 0.08339881896972656 sec
# cwmbp:eval_thread $ python perf.py 1000000 6
# counting 1000000 using 6 threads.
# 0.08277416229248047 sec


from threading import Thread
from time import time

import sys

count, n = sys.argv[1:3]
count, n = int(count), int(n)
print('counting %d using %d threads.' % (count, n))

def count_down(count):
    while count > 0:
        count -= 1

if n == 1:
    start = time()
    count_down(count)
    end = time()

else:
    threads = [Thread(target=count_down, args=(count//n,)) for _ in range(n)]

    start = time()
    for t in threads: t.start()
    for t in threads: t.join()
    end = time()

print(end-start,'sec')
