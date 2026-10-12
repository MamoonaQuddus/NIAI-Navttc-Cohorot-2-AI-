import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

zeros = np.zeros((2,3))
print(zeros)

rand = np.random.randint(1, 10, 5)
print(rand)



# task 1
# import Week3_Day1.n as np
arr2 = np.array([5, 4,3,2,1])
print(arr)


# task 2
zeros = np.ones((3,3))
print(zeros)

rand = np.random.randint(1, 10, 5)
print(rand)


# attribute 

a = np.array([[1,2,3,4,5], [1,2,3,4,5]])
print(arr)

print(a.shape)
print(a.size)
print(a.dtype)
print(a.ndim)

# task 
i = np.array([1,2,3])

c_copy = i.copy()
print(c_copy)

c_copy[0] = 99

print(c_copy)

print(i, c_copy)

g = np.array([1,2,3])
print(np.append(g , [4,5,6]))
print(g)
print(np.insert(g , 1,100))
print(g)

# task
p = np.array([4,3,2])

print(p)
print()
p_copy = p.copy()
print(p)

# task2
q = np.array([1,2,3])
print(np.append(q , [4,5,6]))
print(np.insert(q , 1,100))

# next work
s = np.array([5,3,4,5])
print(s)
print(np.sort(s))
print(s)
print()
print(np.delete(s,0))

f1, f2 = np.array([1,2]) ,np.array([3,4])

print(np.concatenate((f1 , f2)))

print(np.array_split(np.arange(1,7),3))

# Data loading and saving
l = np.array([1,2,3,3])
np.save('my_array.npy', l)


loaded = np.loaded('my_array.npy')
print(loaded)

# 2d,logical
ll= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ll[1,2])
print(ll[g > 5])

# task 1
gg= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(gg[2,1])

# task 2
print(gg[g > g/2])


# braodcasting
a1 = np.array([1,2,3,4,5])
print(a1 + 10)


# task 2

# type casting and Arithmetic

b2 = np.array([1.5, 2.5, 5.5])
print(b2.astype(int))

a2 = np.array([1,2,3,4,5])
a3 = np.array([3,4,5,6,6])

print( a2 -a3, a2 + a3 , a2 * a3)
print(a2 / a3  , a2**2)



# task1
b2 = np.array([2.5, 3.5, 5.5])
print(b2.astype(int))

# task 2

a4 = np.array([1,2,3,4])
a6 = np.array([3,4,5,6])

print( a4 -a6, a4 + a6 , a4 * a6 , a4 / a6)


# universal array function


mm = np.array([1,3,4,5])
print(np.sqrt(mm))

mm = np.array([1,2])
print(np.exp(mm))
print(np.sin(mm))

