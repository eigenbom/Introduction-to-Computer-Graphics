from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from camera import *

MS_PER_FRAME = 10
millis = 0

width, height = 600, 600
mouse = [0,0]

camera = None

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
	global camera

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	camera.set_fov(120.*mouse[1]/height)
	camera.select((0,0,width,height))

	draw_axis()
	draw_cube()

	glFlush()

def init():
	global camera
	camera = PerspectiveCamera(60)
	camera.set_position((10,10,20))
	camera.set_target((0,0,0))
	camera.set_near(1)
	camera.set_far(100)

	glClearColor(0,0,0,0)
	glEnable(GL_DEPTH_TEST)

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

