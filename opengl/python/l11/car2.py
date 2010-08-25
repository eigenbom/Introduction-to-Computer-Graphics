from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

MS_PER_FRAME = 10
millis = 0

width, height = 600, 600
mouse = [0,0]

viewer = [60,8] # rotation around z and height

wireframe = False

def draw_wheel():
	""" Draws a wheel of radius 1, centered at the origin, in the x-y plane """
	outer_radius = 1
	thickness = .4
	if wireframe:
		glutWireTorus(thickness,outer_radius - thickness,8,8)
	else:
		glutSolidTorus(thickness,outer_radius - thickness,8,8)
		glPushAttrib(GL_CURRENT_BIT)
		glPushAttrib(GL_LIGHTING_BIT)
		glDisable(GL_LIGHTING)
		glColor3f(0,0,0)
		glutWireTorus(thickness+.01,outer_radius - thickness + 0.005,8,8)	
		glPopAttrib()
		glPopAttrib()


def draw_car_body():
	""" Draws the car body. It is a 1x1x2 cube with its base at the origin. """
	# draw the car body	
	glPushMatrix()
	glTranslatef(0,.5,0)
	glScalef(1,1,2)
	if wireframe:
		glutWireCube(1)
	else:
		glutSolidCube(1)
		# draw the wireframe outer shell
		glPushAttrib(GL_CURRENT_BIT)
		glPushAttrib(GL_LIGHTING_BIT)
		glDisable(GL_LIGHTING)
		glColor3f(0,0,0)
		glutWireCube(1.001)	
		glPopAttrib()
		glPopAttrib()
	glPopMatrix()

def draw_car():
	""" Draws a car. The 'car' is a 1x1x2 cube with its base at the origin, with wheels at the four corners."""
	wheel_radius = .5
	wheel_thickness = .4

	glPushMatrix()

	# shift the car up so the base lies at the origin
	glTranslatef(0,wheel_radius,0)
	
	draw_car_body()

	# draw the car wheels
	# assume the car is facing down the -z axis
	# front left, front right, back left, back right
	ww = wheel_thickness/2
	wheel_centers = [(-.5-ww,0,-1),(.5+ww,0,-1),(-.5-ww,0,1),(.5+ww,0,1)]
	for i in range(4):
		glPushMatrix()
		apply(glTranslatef,wheel_centers[i])
		glRotatef(90,0,1,0)
		glScalef(wheel_radius,wheel_radius,wheel_radius)
		draw_wheel()
		glPopMatrix()

	glPopMatrix()

def draw_axis():
	glBegin(GL_LINES)
	for v in [(1,0,0),(0,1,0),(0,0,1)]:
		glColor3fv(v)
		glVertex3f(0,0,0)
		glVertex3fv(v)
	glEnd()

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	
	gluLookAt(0,viewer[1],3,0,0,0,0,1,0)	
	glRotatef(viewer[0],0,1,0)
	glLightfv(GL_LIGHT0,GL_POSITION,(10,20,10,1))
	
	draw_axis()
	
	glColor3f(.5,.5,.5)
	draw_car()

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

