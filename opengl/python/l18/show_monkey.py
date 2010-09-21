from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height = 600, 600
mouse = [0,0]

from geometry import *

monkey = None # GeometricModel

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	
	gluLookAt(2,2,2,0,0,0,0,1,0)
	glColor3f(0.5,0.5,1)	
	glLightfv(GL_LIGHT0,GL_POSITION,[2.1,5.2,2.3])
	glRotatef(3*360.*mouse[0]/width,0,1,0)

	monkey.draw()

	glFlush()

def init():
	global monkey
	monkey = ObjFile('monkey.obj').get_geometry()

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
	glutCreateWindow("monkey time!")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutMainLoop()

