import time
import random

a = range(1000)
a = random.sample(a, len(a))
b = range(1000)
b = random.sample(b, len(b))

start_time = time.time()

# min_a = min(a)
# max_a = max(a)
# min_b = min(b)
# max_b = max(b)

min_a = None
max_a = None
min_b = None
max_b = None

for i in a:
    min_a = i if min_a == None or i < min_a else min_a
    max_a = i if max_a == None or i > max_a else max_a

print min_a, max_a

print '%s' % (time.time() - start_time)