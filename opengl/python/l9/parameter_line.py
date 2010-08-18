from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height = 600, 600
mouse = [0,0]

def line(t):
	p = (0,0)
	q = (1.0*mouse[0]/width,1.0*mouse[1]/height)
	return ((1-t)*p[0] + t*q[0], 
					(1-t)*p[1] + t*q[1])

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,1,1)
	glBegin(GL_POINTS)
	for i in range(100):
		t = i/100.
		glVertex2fv(line(t))
	glEnd()
	glFlush()

def init():
	glClearColor(0,0,0,0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,1,0,1)
	glMatrixMode(GL_MODELVIEW)

	glPointSize(2)

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

