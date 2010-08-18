from OpenGL.GL import *
from OpenGL.GLUT import *
from random import random

width, height = 600, 600

def displayBitmapString(string):
	for s in string:
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(s))

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	
	for i in range(10):
		glColor3f(random(),random(),random());
		glRasterPos2f(0.1,i*.1)	
		displayBitmapString("Computer graphics is AWESOME!");	
	
	glFlush()

def resize(w,h):
	global width, height
	width = w
	height = h

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
	glutCreateWindow("text")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutMainLoop()

