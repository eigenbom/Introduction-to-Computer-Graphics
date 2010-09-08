from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from cube import Cube

MS_PER_FRAME = 10
millis = 0

width, height = 600, 600
mouse = [0,0]

# switch between DEPTH, NO_DEPTH_NO_CULL, NO_DEPTH_CULL
NUM_MODES = 3
M_DEPTH, M_NO_DEPTH_NO_CULL, M_NO_DEPTH_CULL = range(NUM_MODES)
mode_labels = {M_DEPTH:"Depth buffer enabled.", M_NO_DEPTH_NO_CULL: "No depth buffer, no backface culling.", M_NO_DEPTH_CULL: "No depth buffer, backface culling."}

mode = M_DEPTH



def draw_axis():
	glBegin(GL_LINES)
	for v in [(1,0,0),(0,1,0),(0,0,1)]:
		glColor3fv(v)
		glVertex3f(0,0,0)
		glVertex3fv(v)
	glEnd()

def displayBitmapString(string):
	for s in string:
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(s))

def display():
	global mode_labels, mode

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	
	glLoadIdentity()

	gluLookAt(1,2,3,0,0,0,0,1,0)	
	draw_axis()
	glRotatef(360.*millis*0.001*.2,1,0,0)
	glRotatef(360.*millis*0.001*.07,0,1,0)
	Cube.draw()
	 
	glMatrixMode(GL_PROJECTION)
	glPushMatrix()
	glLoadIdentity()
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	glColor3f(1,1,1)
	glRasterPos(-.2,-.9)
	displayBitmapString(mode_labels[mode])

	glMatrixMode(GL_PROJECTION)
	glPopMatrix()
	glMatrixMode(GL_MODELVIEW)

	glFlush()

def update_mode():
	if mode==M_DEPTH:
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_CULL_FACE)
	elif mode==M_NO_DEPTH_NO_CULL:
		glDisable(GL_DEPTH_TEST)
		glDisable(GL_CULL_FACE)
	elif mode==M_NO_DEPTH_CULL:
		glDisable(GL_DEPTH_TEST)
		glEnable(GL_CULL_FACE)

def init():
	glClearColor(0,0,0,0)
	
	update_mode()

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
	global mode
	mode = (mode + 1) % NUM_MODES
	update_mode()
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

