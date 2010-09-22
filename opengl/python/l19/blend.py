#
# Demonstrates basic GL blending.
# BP 22.09.2010
#

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from random import random

MS_PER_FRAME = 10
millis = 0

width, height = 600, 600
mouse = [0,0]

# A square is an [x,y,x',y',colour] tuple
# that floats around the space
NUM_SQUARES = 100
SQUARE_SIZE = .1
SQUARE_SPEED = .1
MAX_SQUARE_ALPHA = .5
squares = [[random(),random(),0,0,(random(),random(),random(),MAX_SQUARE_ALPHA*random())] for i in range(NUM_SQUARES)]

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()

	for sq in squares:
		glColor4fv(sq[4])
		glRectf(sq[0]-SQUARE_SIZE/2,sq[1]-SQUARE_SIZE/2,
				sq[0]+SQUARE_SIZE/2,sq[1]+SQUARE_SIZE/2)

	glFlush()

def move_squares():
	for sq in squares:
		sq[0] += sq[2]*SQUARE_SPEED
		sq[1] += sq[3]*SQUARE_SPEED
		# always attracted to the center (.5,.5)
		x_attract = .5-sq[0]
		y_attract = .5-sq[1]

		sq[2] += x_attract*random()*.001
		sq[3] += y_attract*random()*.001

def init():
	glClearColor(1,1,1,1)
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,1,0,1)
	glMatrixMode(GL_MODELVIEW)

def resize(w,h):
	global width, height
	width, height = w,h
	glViewport(0,0,w,h)
	glutPostRedisplay()

def motion(x,y):
	global mouse
	mouse = x, y
	glutPostRedisplay()

def timer(i):
	global millis
	millis += MS_PER_FRAME
	move_squares()
	glutPostRedisplay()
	glutTimerFunc(MS_PER_FRAME,timer,0)

def key(key,x,y):
	glutPostRedisplay()

def keysp(key,x,y):
	glutPostRedisplay()

if __name__=="__main__":
	glutInit()
	glutInitWindowSize(width,height)
	glutInitDisplayMode(GLUT_DEPTH)
	glutCreateWindow(".")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutKeyboardFunc(key)
	glutSpecialFunc(keysp)
	glutTimerFunc(MS_PER_FRAME,timer,0)
	glutMainLoop()

