import numpy as np
import math

def mat():
	a = np.matrix('1, 2, 3; 2, 7, 4')
	b = np.matrix('1, -1; 0, 1')
	c = np.matrix('5, -1; 9, 1; 6, 0')	
	d = np.matrix('3, -2, -1; 1, 2, 3')
	u = np.matrix('6, 2, -3, 5')
	v = np.matrix('3, 5, -1, 4')
	w = np.matrix('1; 8; 0; 5')

	print('A = ','\n',a,'\n')
	print('B = ','\n',b,'\n')
	print('C = ','\n',c,'\n')
	print('D = ','\n',d,'\n')
	print('u = ','\n',u,'\n')
	print('v = ','\n',v,'\n')
	print('w = ','\n',w,'\n')
	
	adim = a.shape
	bdim = b.shape
	cdim = c.shape
	ddim = d.shape
	udim = u.shape
	vdim = v.shape
	wdim = w.shape

	print('Section 1')
	print('1.1. The dimensions of A are', adim)
	print('1.2. The dimensions of B are', bdim)
	print('1.3. The dimensions of C are', cdim)
	print('1.4. The dimensions of D are', ddim)
	print('1.5. The dimensions of u are', udim)
	print('1.6. The dimensions of v are', vdim)
	print('1.7. The dimensions of w are', wdim)

	dtproduct = np.inner(u,v)
	sqru = math.sqrt((u.item(0,0)**2) + (u.item(0,1)**2) + (u.item(0,2)**2) + (u.item(0,3)**2))
	
	print()
	print('Section 2')
	print('2.1. u + v =', (u+v))
	print('2.2. u - v =', (u-v))
	print('2.3. au where a=6 =', (6*u))
	print('2.4. u * v =', dtproduct)
	print('2.5. ||u|| =', sqru)

	
	'''try:
		smac = a + c
	except ValueError:
		print('not defined')'''
  '''    @klq I know I should be able to get each matrix to pass an exception and print out 'not defined'. I couldn't quite figure out how to do that right now, but I'm still working on these.
	'''
	
	trsna = a.getT()
	print()
	print('Section 3')
	print('3.1. A +C =', '\n', 'not defined', '\n')
	print('3.2. A - Ct =', '\n', (a - c.getT()), '\n')
	print('3.3. Ct + 3D =', '\n', (c.getT() + 3*d), '\n')
	print('3.4. BA =', '\n', (b*a), '\n')
	#print('3.5. BAt =', '\n', b.dot(trsna), '\n')
	print('3.5. BAt =', '\n', 'not defined', '\n')
	#print('3.6. BC =', '\n', (b*c), '\n')
	print('3.6. BC =', '\n', 'not defined', '\n')
	print('3.7. BA =', '\n', (b*a), '\n')



def main():
	mat()

if __name__ == '__main__':
	main()
