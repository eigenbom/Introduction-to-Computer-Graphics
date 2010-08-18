from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height = 600, 600
mouse = [0,0]

def concavedata():
	glVertex2f(.25,.25)
	glVertex2f(.75,.25)
	glVertex2f(.5,.5)
	glVertex2f(.75,.75)
	glVertex2f(.25,.75)
	glVertex2f(1.0*mouse[0]/width,1.0*mouse[1]/height)

def concavepolyfill():
	glBegin(GL_POLYGON)
	concavedata()
	glEnd()

def concavepolylines():
	glBegin(GL_LINE_LOOP)
	concavedata()
	glEnd()

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	
	glColor3f(0,0,1)
	concavepolyfill()

	glColor3f(1,1,1)
	concavepolylines()
	
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
	glutPostRedisplay()

def motion(x,y):
	global mouse
	mouse = x, height-y
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

