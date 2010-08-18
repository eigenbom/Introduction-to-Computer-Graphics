from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import random

width, height = 600, 600
mouse = [0,0]
colours = [[random(),random(),random()] for i in range(10)]

def displayStrokeString(string):
	glPushMatrix()
	for s in string:
		glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, ord(s))
	glPopMatrix()

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glPushMatrix()
	glPushAttrib(GL_LINE_BIT)

	glScalef(.001,.001,1)
	glRotatef(360.*mouse[0]/width,0,0,1)

	NUM_HELLOS = 10
	for i in range(NUM_HELLOS):
		glLineWidth(min(4,i+1))
		glColor3fv(colours[i]);
		glRotatef(360./NUM_HELLOS,0,0,1)
		glPushMatrix()
		glTranslatef(200,0,0)
		displayStrokeString("Hello!!");	
		glPopMatrix()

	glPopAttrib()
	glPopMatrix()
	glFlush()

def resize(w,h):
	global width, height
	width = w
	height = h

	glutPostRedisplay()

def motion(x,y):
	global mouse
	mouse = x,y

	glutPostRedisplay()

def init():
	glClearColor(0,0,0,0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-1,1,-1,1)
	glMatrixMode(GL_MODELVIEW)

if __name__=="__main__":
	glutInit()
	glutInitWindowSize(600,600)
	glutCreateWindow("text")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutMainLoop()

