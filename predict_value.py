def predict_value(Theta1, Theta2, frame):
	m = X.shape[0]
	h1 = sigmoid(X.dot(Theta1.T))
	h1 = hstack((ones((m,1)),h1))
	h2 = sigmoid(h1.dot(Theta2.T))
	p = argmax(h2,axis=1)
	return p
# frame should be numpy array without the 1 in the first position,which signifies right hand,
# and without the label value at the last index
from numpy import *
from scipy.special import expit as sigmoid
