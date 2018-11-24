import numpy as np


a = np.random.randn(5)
print(a)
print(a.shape)
#(5,)

print(a.T)

print(np.dot(a,a.T))


#column vector-列向量
b = np.random.randn(5,1)


print("column vector：")
print(b)
print(b.T)

print(np.dot(b,b.T))
#5*5

