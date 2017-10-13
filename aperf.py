# cwmbp:eval_thread $ python aperf.py 1000000 1
# counting 1000000 using 1 coroutines.
# 0.07740211486816406 sec
# cwmbp:eval_thread $ python aperf.py 1000000 2
# counting 1000000 using 2 coroutines.
# 0.07551693916320801 sec
# cwmbp:eval_thread $ python aperf.py 1000000 3
# counting 1000000 using 3 coroutines.
# 0.07536101341247559 sec
# cwmbp:eval_thread $ python aperf.py 1000000 4
# counting 1000000 using 4 coroutines.
# 0.08054184913635254 sec
# cwmbp:eval_thread $ python aperf.py 1000000 5
# counting 1000000 using 5 coroutines.
# 0.08318424224853516 sec
# cwmbp:eval_thread $ python aperf.py 1000000 6
# counting 1000000 using 6 coroutines.
# 0.07696700096130371 sec
# cwmbp:eval_thread $ python aperf.py 1000000 7
# counting 1000000 using 7 coroutines.
# 0.07838010787963867 sec

from asyncio import get_event_loop, gather
import sys
from time import time

count, n = sys.argv[1:3]
count, n = int(count), int(n)
print(f'counting {count} using {n} coroutines.')

async def count_down(count):
    while count > 0:
        count -= 1
    return

async def count_down_coro(count):
    await count_down(count)

loop = get_event_loop()
tasks = [loop.create_task(count_down_coro(count//n)) for _ in range(n)]

try:
    start = time()
    loop.run_until_complete(gather(*tasks))
    end = time()
finally:
    loop.close()
    print(end-start,'sec')
