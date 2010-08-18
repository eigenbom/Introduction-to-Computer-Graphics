from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height = 600, 600
mouse = [0,0]

BOX_ID = 0

def build_red_box():
	global BOX_ID
	BOX_ID = glGenLists(1)
	glNewList(BOX_ID, GL_COMPILE)
	glPushAttrib(GL_CURRENT_BIT)
	glColor3f(1,0,0)
	glBegin(GL_QUADS)
	glVertex2f(.25,.25)
	glVertex2f(.75,.25)
	glVertex2f(.75,.75)
	glVertex2f(.25,.75)
	glEnd()
	glPopAttrib()
	glEndList()

def red_box():
	glCallList(BOX_ID)

def box():
	glBegin(GL_QUADS)
	glVertex2f(.25,.25)
	glVertex2f(.75,.25)
	glVertex2f(.75,.75)
	glVertex2f(.25,.75)
	glEnd()

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glPushMatrix()

	# set the colour to blue
	glColor3f(0,0,1)
	
	# draw a red box
	red_box()

	# red_box has pushed and popped the attribute stack, 
	# and so now glColor is set back to blue
	glScale(.5,.5,1)
	box()
	
	glPopMatrix()
	glFlush()

def init():
	glClearColor(0,0,0,0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,1,0,1)
	glMatrixMode(GL_MODELVIEW)

	build_red_box()

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

