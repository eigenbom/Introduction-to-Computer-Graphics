from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height = 600, 600
mouse = [0,0]

def tesserror(errno):
	print("ohno!")

def tesscomb(c,vd,w):
	return c

def tessellateConcavePoly():
	tess = gluNewTess()
	gluTessCallback(tess, GLU_TESS_BEGIN, glBegin)
	gluTessCallback(tess, GLU_TESS_END, glEnd)
	gluTessCallback(tess, GLU_TESS_VERTEX, glVertex3dv)
	gluTessCallback(tess, GLU_TESS_ERROR, tesserror)
	gluTessCallback(tess, GLU_TESS_COMBINE, tesscomb)
	gluTessBeginPolygon(tess,None)
	gluTessBeginContour(tess)
	vertices = [[.25,.25],[.75,.25],[.5,.5],[.75,.75],[.25,.75],[1.0*mouse[0]/width,1.0*mouse[1]/height]]
	for v in vertices:
		v3 = [v[0],v[1],0]
		gluTessVertex(tess,v3,v3)
	gluTessEndContour(tess)
	gluTessEndPolygon(tess)


def concavedata():
	glVertex2f(.25,.25)
	glVertex2f(.75,.25)
	glVertex2f(.5,.5)
	glVertex2f(.75,.75)
	glVertex2f(.25,.75)
	glVertex2f(1.0*mouse[0]/width,1.0*mouse[1]/height)

def concavepolylines():
	glBegin(GL_LINE_LOOP)
	concavedata()
	glEnd()

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	
	glColor3f(0,0,1)
	tessellateConcavePoly()
	
	glColor3f(1,1,1)
	concavepolylines()
	glFlush()

def init():
	glClearColor(0,0,0,0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,1,0,1)
	glMatrixMode(GL_MODELVIEW)

def resize(w,h):
	global width, height
	width, height = w,h
	glViewport(0,0,w,h)
	glutPostRedisplay()

def motion(x,y):
	global mouse
	mouse = x, height-y
	glutPostRedisplay()

if __name__=="__main__":
	glutInit()
	glutInitWindowSize(width,height)
	glutCreateWindow(".")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutMainLoop()

