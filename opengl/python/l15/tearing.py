#
# This example doesn't work.
# I couldn't figure out how to disable VSYNC
# BP 2010
#

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from OpenGL.WGL import (wglSwapIntervalEXT,wglGetSwapIntervalEXT)

from cube import Cube
import math

MS_PER_FRAME = 20
millis = 0

width, height = 600, 600
mouse = [0,0]

def draw_axis():
	glBegin(GL_LINES)
	for v in [(1,0,0),(0,1,0),(0,0,1)]:
		glColor3fv(v)
		glVertex3f(0,0,0)
		glVertex3fv(v)
	glEnd()

def draw_cube():
	glPushMatrix()
	glColor3f(1,1,1)
	glutWireCube(1)
	glPopMatrix()


def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	gluLookAt(0,1,2,0,0,0,0,1,0)	

	draw_axis()
	glTranslatef(0.2*math.sin(360.0*millis*0.001*0.005),0,0)
	#glRotatef(360.*millis*0.001*0.1,1,1,1)
	#Cube.draw()
	for i in range(1000):
		draw_cube()

	glFlush()

def init():
	# Disable vsync for the purposes of this demo
	if (bool)(wglSwapIntervalEXT):
		wglSwapIntervalEXT(0)
	else:
		print("Cannot disable vsync!")
		print("Current value: %d"%wglGetSwapIntervalEXT())
	
	glClearColor(0,0,0,0)
	glEnable(GL_DEPTH_TEST)

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
	mouse = x, y
	glutPostRedisplay()

def idle():
	glutPostRedisplay()

def timer(i):
	global millis
	millis += MS_PER_FRAME
	glutPostRedisplay()
	glutTimerFunc(MS_PER_FRAME,timer,0)

def key(key,x,y):
	glutPostRedisplay()

def keysp(key,x,y):
	glutPostRedisplay()

if __name__=="__main__":
	print("This example doesn't work. It is meant to illustrate tearing, but I couldn't figure out how to disable vsync.")
	exit()

	glutInit()
	glutInitWindowSize(width,height)
	glutInitDisplayMode(GLUT_DEPTH | GLUT_SINGLE)
	glutCreateWindow(".")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutKeyboardFunc(key)
	glutSpecialFunc(keysp)
	glutIdleFunc(idle)
	glutTimerFunc(MS_PER_FRAME,timer,0)
	glutMainLoop()

