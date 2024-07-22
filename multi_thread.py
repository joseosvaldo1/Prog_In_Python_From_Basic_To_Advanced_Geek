# Exemplo_2 - Dois thread em pararelo:

import time
from threading import Thread


COUNTER = 50000000


def time_countdown(n):
	while n > 0:
		n -= 1


t1 = Thread(target=time_countdown, args=(COUNTER // 2, ))
t2 = Thread(target=time_countdown, args=(COUNTER // 2, ))

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Time interval in s - multi thread: "
      f"{end - start} s.") # => Time interval in s - multi thread:
# 7.191229820251465 s.
