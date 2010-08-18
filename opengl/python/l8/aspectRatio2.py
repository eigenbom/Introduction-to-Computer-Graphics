from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height = 600, 600
mouse = [0,0]

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	# draw a checkboard, 8x8 in a unit square
	tw = 1./8 # tileWidth
	for row in range(8):
		for col in range(8):
			if ((row+col)%2==0):
				glColor3f(1,1,1)
			else:
				glColor3f(0,0,0)
			glRectf(col*tw,row*tw,col*tw+tw,row*tw+tw)

	glFlush()

def init():
	glClearColor(0,0,0,0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,1,0,1)
	glMatrixMode(GL_MODELVIEW)

def resize(w,h):
	global width, height
	width, height = w,h

	glViewport(0,0,w,h)
	
	# need to maintain the correct aspect ratio	
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,1,0,1.0*height/width)
	glMatrixMode(GL_MODELVIEW)

	glutPostRedisplay()

def motion(x,y):
	global mouse
	mouse = x,y
	glutPostRedisplay()

if __name__=="__main__":
	glutInit()
	glutInitWindowSize(width,height)
	glutCreateWindow(".")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutMainLoop()

