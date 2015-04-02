import numpy as np
import matplotlib.pyplot as plt

class lenError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
		 
def rangef(min, max, step):
	result = []
	while 1:
		result.append(min)
		min = min+step
		if min>=max:
			break
	return result

def bezier3((x1,y1),(x2,y2),(x3,y3),(x4,y4)):
	x = []
	y = []
	bx = 3*(x2-x1)
	cx = 3*(x3-x2)-bx
	dx = x4-x1-bx-cx
	by = 3*(y2-y1)
	cy = 3*(y3-y2)-by
	dy = y4-y1-by-cy
	for t in rangef(0,1,0.2):
		x.append(x1+bx*t+cx*(t**2)+dx*(t**3))
		y.append(y1+by*t+cy*(t**2)+dy*(t**3))
	return (x,y)


def bezier(*args):
	x = []
	y = []
	try:
		if (len(args)-1)%3 != 0:
			raise lenError(len(args))
	except lenError as e:
		print "length of args " + str(e.value) + " is not 1+3n"
	argcount = 0
	while(argcount < len(args)-1):
		bez = bezier3(args[argcount],args[argcount+1],args[argcount+2],args[argcount+3])
		x.extend(bez[0])
		y.extend(bez[1])
		argcount = argcount + 3
	plt.plot(np.array(x), np.array(y))
	
	#t = 1/3
	#(1-t)*bezier2(t,

def main():
	bezier((1,2),(2,3),(4,5),(6,7))
	
main()