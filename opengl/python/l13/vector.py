import math

def cross_product((a1,a2,a3),(b1,b2,b3)):
	return (a2*b3-a3*b2, a3*b1-a1*b3,	a1*b2-a2*b1)

def vect_add((a1,a2,a3),(b1,b2,b3)):
	return (a1+b1,a2+b2,a3+b3)

def vect_mult((a1,a2,a3),b):
	return (a1*b,a2*b,a3*b)

def vect_len((a1,a2,a3)):
	return math.sqrt(a1*a1+a2*a2+a3*a3)
	
