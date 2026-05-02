import numpy as np
#question 1 : create an array of numbers from 1 to 5 and add 10 to each element using broadcasting
a = np.array([1,2,3,4,5])
b = 10
print(a + b)


# question 2 : add c to each column of d
c = np.array([[1,2,3],
              [4,5,6]])
d = np.array([10,20,30])
print(c + d)


# question 3 : add f to each row of e
e = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
f = np.array([[10], [20], [30]])
print(e + f)


