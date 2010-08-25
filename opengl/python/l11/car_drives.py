"""
A demo of a car driving in a straight line.
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from car_module import Car

width, height = 600, 600
MS_PER_FRAME = 10
viewer = [60,8] # rotation around z and height

millis = 0
mouse = [0,0]
wireframe = False

car = Car((1,0,0))
car.set_wheel_rotation_speed(0.1) # rotations per second 

def draw_axis():
	glBegin(GL_LINES)
	for v in [(1,0,0),(0,1,0),(0,0,1)]:
		glColor3fv(v)
		glVertex3f(0,0,0)
		glVertex3fv(v)
	glEnd()


def draw_grid():
	""" draws a grid of 100x100 on the x-z plane with 1 unit increments """
	glPushAttrib(GL_LIGHTING_BIT)
	glDisable(GL_LIGHTING)

	glColor3f(.8,.8,.8)
	glBegin(GL_LINES)
	# draw along the x axis
	for z in range(-100,101,1):
		glVertex3f(-100,0,z)
		glVertex3f(100,0,z)
	for x in range(-100,101,1):
		glVertex3f(x,0,-100)
		glVertex3f(x,0,100)
	glEnd()

	glPopAttrib()


def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	
	gluLookAt(car.pos[0],car.pos[1]+viewer[1],car.pos[2]+viewer[1],car.pos[0],car.pos[1],car.pos[2],0,1,0)	
	
	glTranslatef(car.pos[0],car.pos[1],car.pos[2])
	glRotatef(viewer[0],0,1,0)
	glTranslatef(-car.pos[0],-car.pos[1],-car.pos[2])
	
	# move camera to rotate around car
	#glTranslatef(car.pos[0],0,car.pos[2])	
	#gluLookAt(ca,viewer[1],3,0,0,0,0,1,0)	
	#glTranslatef(-car.pos[0],0,-car.pos[2])	
	
	glLightfv(GL_LIGHT0,GL_POSITION,(10,20,10,1))
	
	draw_axis()
	draw_grid()

	car.draw(wireframe)

	glFlush()

def init():
	glClearColor(1,1,1,1)
	glEnable(GL_DEPTH_TEST)
	
	# turn on lighting
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)	
	glEnable(GL_COLOR_MATERIAL)
	glEnable(GL_NORMALIZE)
	glColorMaterial(GL_FRONT,GL_DIFFUSE)
	glLightfv(GL_LIGHT0,GL_AMBIENT,(0,0,0,1))
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT,(.2,.2,.2,1))
	
	# enable flat shading
	glShadeModel(GL_FLAT)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60,1,0.1,100)
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
	car.update(0.001 * MS_PER_FRAME)
	glutPostRedisplay()
	glutTimerFunc(MS_PER_FRAME,timer,0)

def key(key,x,y):
	global wireframe
	if (key=='w'): wireframe = not wireframe
	glutPostRedisplay()

def keysp(key,x,y):
	global viewer	
	if key==GLUT_KEY_LEFT:
		viewer[0] -= 10
	elif key==GLUT_KEY_RIGHT:
		viewer[0] += 10
	elif key==GLUT_KEY_DOWN:
		viewer[1] -= 1
	elif key==GLUT_KEY_UP:
		viewer[1] += 1
	glutPostRedisplay()

if __name__=="__main__":
	glutInit()
	glutInitWindowSize(width,height)
	glutInitDisplayMode(GLUT_DEPTH)
	glutCreateWindow("car example")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutKeyboardFunc(key)
	glutSpecialFunc(keysp)
	glutTimerFunc(MS_PER_FRAME,timer,0)
	glutMainLoop()

