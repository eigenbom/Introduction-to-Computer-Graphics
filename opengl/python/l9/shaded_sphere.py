from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height = 600, 600
mouse = [0,0]

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	gluLookAt(2,2,2,0,0,0,0,1,0)
	glColor3f(1,1,0)	
	glLightfv(GL_LIGHT0,GL_POSITION,[2.1,2.2,2.3])
	glRotatef(3*360.*mouse[0]/width,0,1,0)
	glutSolidSphere(1,8,8)
	glColor3f(0,0,0)
	glScalef(1.01,1.01,1.01)
	glutWireSphere(1,8,8)

	glFlush()

def init():
	glClearColor(0,0,0,0)

	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_COLOR_MATERIAL)
	glColorMaterial(GL_FRONT,GL_DIFFUSE)

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
	glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH)
	glutCreateWindow("shaded sphere")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutMainLoop()

