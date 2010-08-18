from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height = 600, 600
mouse = [0,0]

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	gluLookAt(-1+2.*mouse[0]/width,2,2,0,0,0,0,1,0)	
	glColor3f(1,1,1)
	glutWireCube(1)
	glFlush()

def init():
	glClearColor(0,0,0,0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60,1,0.1,10)
	glMatrixMode(GL_MODELVIEW)

def resize(w,h):
	global width, height
	width, height = w,h
	glViewport(0,0,w,h)
	glutPostRedisplay()

def motion(x,y):
	global mouse
	mouse = x,y
	glutPostRedisplay()

if __name__=="__main__":
	glutInit()
	glutInitWindowSize(width,height)
	glutCreateWindow("cube")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutMainLoop()

