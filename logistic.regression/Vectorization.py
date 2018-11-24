import numpy as np

import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

print(a)

tic = time.time()

c = np.dot(a,b)
toc = time.time()

print(c)

print("Vectorized version:" + str(1000*(toc - tic))+"ms")

c = 0

tic = time.time()

for i in range(1000000):
    c += a[i]*b[i]


toc = time.time()


print(c)

print("For loop version:" + str(1000*(toc - tic))+"ms")


#执行结果
#24960.917817827663
#Vectorized version:0.7839202880859375ms
#24960.91781782775
#For loop version:433.9430332183838ms
#相差600倍
