from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height = 600, 600
mouse = [0,0]

colours = {"red":(1,0,0),"blue":(0,0,1),"green":(0,1,0),
					"yellow":(1,1,0),"magenta":(1,0,1),"cyan":(0,1,1),
					"white":(1,1,1), "black":(0,0,0)}

# A 1x1x1 Cube centered at [.5,.5,-.5]
class Cube(object):
	vertices = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),
							(0,0,-1),(1,0,-1),(1,1,-1),(0,1,-1)]
	faces = [(0,1,2,3),(1,5,6,2),(4,5,6,7),
					 (4,0,3,7),(4,5,1,0),(3,2,6,7)]
	face_colours = [colours[c] for c in ["red","blue","green","yellow","magenta","cyan"]]
	@staticmethod
	def draw():
		glBegin(GL_QUADS)
		for f in Cube.faces:
			glColor3fv(Cube.face_colours[Cube.faces.index(f)])
			for v in f:
				glVertex3fv(Cube.vertices[v])
		glEnd()


def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	gluLookAt(-2+5.*mouse[0]/width,2,2,.5,.5,-.5,0,1,0)	
	glColor3f(1,1,1)
	glTranslatef(.5,.5,-.5)
	glRotatef(360.*mouse[1]/height,1,0,0)
	glTranslatef(-.5,-.5,.5)
	Cube.draw()

	glFlush()

def init():
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
	mouse = x,y
	glutPostRedisplay()

if __name__=="__main__":
	glutInit()
	glutInitWindowSize(width,height)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH)
	glutCreateWindow("cube")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutMainLoop()

