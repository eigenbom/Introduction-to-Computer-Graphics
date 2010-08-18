from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height = 600, 600
mouse = [0,0]

BOX_ID = 0

def build_box():
	global BOX_ID
	BOX_ID = glGenLists(1)
	glNewList(BOX_ID, GL_COMPILE)
	glBegin(GL_QUADS)
	glVertex2f(.25,.25)
	glVertex2f(.75,.25)
	glVertex2f(.75,.75)
	glVertex2f(.25,.75)
	glEnd()
	glEndList()

def box():
	glCallList(BOX_ID)

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	box()
	glFlush()

def init():
	glClearColor(0,0,0,0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,1,0,1)
	glMatrixMode(GL_MODELVIEW)

	build_box()

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
	glutCreateWindow("display list")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutMainLoop()

