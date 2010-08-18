from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *

width, height = 600, 600
mouse = [0,0]

def circle(segments):
	ds = 360.0/segments
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(0,0)
	for i in range(segments+1):
		angle = radians(i*ds)
		x = cos(angle)
		y = sin(angle)
		glVertex2f(x,y)
	glEnd()

def box():
	glBegin(GL_QUADS)
	glVertex2f(0,0)
	glVertex2f(1,0)
	glVertex2f(1,1)
	glVertex2f(0,1)
	glEnd()
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glPushMatrix()


	glTranslatef(.5,.5,0)
	glScalef(.2+1.0*mouse[1]/height,.2+1.0*mouse[1]/height,1)
	
	colors = [[1,0,0],[0,1,0],[0,0,1]]
	for i in range(3):
		glColor3fv(colors[i])
		glPushMatrix()
		glRotatef(i*120,0,0,1)
		glTranslatef(1.0*mouse[0]/width,0,0)
		circle(64)
		glPopMatrix()
	glPopMatrix()
	glFlush()

def resize(w,h):
	global width, height
	width = w
	height = h
	glViewport(0,0,w,h)

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
	
	glEnable(GL_BLEND)
	glBlendFunc(GL_ONE,GL_ONE)

if __name__=="__main__":
	glutInit()
	glutInitWindowSize(600,600)
	glutCreateWindow("additive color blending")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(mouseMoved)
	glutMainLoop()

