import numpy
import time

n= 512
a = numpy.random.randint(50, size=(n,n))
b = numpy.random.randint(50, size=(n,n))
# print(a)
# print(b)
M = a*0
t = time.time()
for k in range (n) :
    for j in range(n):
        for i in range (n):
            M[i][j] +=(a[i][k] * b[k][j])
            
#M = a.dot(b)
# print (M)
print()
print("In Python with combination k j i")
print (n,"n : Execution time in seconds : ",time.time() - t)
print()