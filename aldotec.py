import random
import sys
import time
def mengetik(s):
   for c in s  + '\n':
	sys.stdout.write(c)
	sys.stdout.flush()

	time.sleep(random.random() * 0.3)

mengetik('Jangab Lupa Bersyukur Kepada HpMu\nSelamat Datang\nTerimakasih.')

