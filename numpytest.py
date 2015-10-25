import numpy as np
test1=np.matrix('1 2 3; 4 5 6; 7 8 9s',float)
test2=np.matrix([[1,2,3],[4,5,6],[7,8,9]],float)
list1=[1,2,3]
list2=[4,5,6]
test3=np.matrix([list1,list2,list1],float)
test4=np.empty(shape=(0,136), dtype=float)
#np.concatenate((test2,[9,12,15]))
#blanktest=np.matrix(1)

a=np.load('filenamestring.npy')
print a
