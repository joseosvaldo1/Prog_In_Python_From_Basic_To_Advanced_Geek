"""
# Como lidar com o GIL do Python:

- Caso você tenha problemas com o GIL, você pode utilizar
multi-processing ao invés de multithreading.
- Utilizando processos ao invés de threads cada processo Python ganha
seu próprio interpretador Python e espaço em memória. Desta forma o
GIL não será problema.


"""


from multiprocessing import Pool
from time import time


COUNTER = 50000000


def time_countdown(n):
	while n > 0:
		n -= 1


if __name__ == '__main__':
	pool = Pool(processes=2)
	start = time()
	r1 = pool.apply_async(time_countdown, [COUNTER // 2])
	r2 = pool.apply_async(time_countdown, [COUNTER // 2])
	pool.close()
	pool.join()
	end = time()

	print(f"Time interval in s - Multiprocessing: "
	      f"{end - start} s")  # => Time interval in s -
	# Multiprocessing: 4.288649797439575 s


