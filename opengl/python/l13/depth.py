from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

MS_PER_FRAME = 10
millis = 0

width, height = 600, 600
mouse = [0,0]

depth_test = True

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
		glPushMatrix()
		glTranslatef(-.5,-.5,.5)
		glBegin(GL_QUADS)
		for f in Cube.faces:
			glColor3fv(Cube.face_colours[Cube.faces.index(f)])
			for v in f:
				glVertex3fv(Cube.vertices[v])
		glEnd()
		glPopMatrix()

def draw_axis():
	glBegin(GL_LINES)
	for v in [(1,0,0),(0,1,0),(0,0,1)]:
		glColor3fv(v)
		glVertex3f(0,0,0)
		glVertex3fv(v)
	glEnd()

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	if depth_test: 
		glClear(GL_DEPTH_BUFFER_BIT)
	
	glLoadIdentity()
	gluLookAt(1,2,3,0,0,0,0,1,0)	

	draw_axis()
	glRotatef(360.*mouse[0]/width,1,0,0)
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
	mouse = x, y
	glutPostRedisplay()

def timer(i):
	global millis
	millis += MS_PER_FRAME
	glutPostRedisplay()
	glutTimerFunc(MS_PER_FRAME,timer,0)

def key(key,x,y):
	global depth_test
	depth_test = not depth_test
	if not depth_test:
		glDisable(GL_DEPTH_TEST)
	else: 
		glEnable(GL_DEPTH_TEST)
	glutPostRedisplay()

def keysp(key,x,y):
	glutPostRedisplay()

if __name__=="__main__":
	glutInit()
	glutInitWindowSize(width,height)
	glutInitDisplayMode(GLUT_DEPTH)
	glutCreateWindow(".")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutKeyboardFunc(key)
	glutSpecialFunc(keysp)
	glutTimerFunc(MS_PER_FRAME,timer,0)
	glutMainLoop()

