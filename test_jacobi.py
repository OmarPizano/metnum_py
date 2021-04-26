from metnum import jacobi

### TEST JACOBI ###
#A = [[5, -2, 1], [3,15,-4], [4,6,20]]
#b = [5,7,8]

A = [[10, 1, 2], [4,6,-1], [-2,3,8]]
b = [3,9,51]

x0 = [0,0,0]
maxi = 20

print(jacobi(A,b,x0))

