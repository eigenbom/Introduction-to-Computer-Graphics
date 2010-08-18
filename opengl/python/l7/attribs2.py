from OpenGL.GL import *
from OpenGL.GLUT import *

width, height = 600, 600
mouse = [0,0]

def box():
	glBegin(GL_QUADS)
	glVertex2f(0,0)
	glVertex2f(1,0)
	glVertex2f(1,1)
	glVertex2f(0,1)
	glEnd()
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	
	for i in range(10):
		for j in range(10):
			glPushMatrix()
			glTranslate(i*.1,j*.1,0)
			glScale(.1,1,1)
			glColor3f(i*.11,j*.11,1.0*mouse[0]/width)
			box()
			glPopMatrix()

	glFlush()

def resize(w,h):
	global width, height
	width = w
	height = h

	glutPostRedisplay()

def mouseMoved(x,y):
	global mouse
	mouse = x, y
	glutPostRedisplay()

def init():
	glClearColor(0,0,0,0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0,1,0,1,-1,1)
	glMatrixMode(GL_MODELVIEW)

if __name__=="__main__":
	glutInit()
	glutInitWindowSize(600,600)
	glutCreateWindow("attributes")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(mouseMoved)
	glutMainLoop()

