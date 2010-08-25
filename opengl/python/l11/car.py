from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

MS_PER_FRAME = 10
millis = 0

width, height = 600, 600
mouse = [0,0]

viewer = [60,4] # rotation around z and height

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
		glColor3f(1,1,1)
		glutWireTorus(thickness+.05,outer_radius - thickness + 0.0025,8,8)	
		glPopAttrib()
		glPopAttrib()

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
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	
	gluLookAt(0,viewer[1],4,0,0,0,0,1,0)	
	glRotatef(viewer[0],0,1,0)
	glLightfv(GL_LIGHT0,GL_POSITION,(10,20,10,1))
	
	draw_axis()
	
	glColor3f(0,0,1)
	
	for i in range(-2,3,2):
		glPushMatrix()
		glTranslatef(0,0,i)
		draw_wheel()
		glPopMatrix()

	glFlush()

def init():
	glClearColor(1,1,1,1)
	glEnable(GL_DEPTH_TEST)
	
	# turn on lighting
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)	
	glEnable(GL_COLOR_MATERIAL)
	glEnable(GL_NORMALIZE)
	#glColorMaterial(GL_FRONT,GL_DIFFUSE)
	glLightfv(GL_LIGHT0,GL_AMBIENT,(0,0,0,1))
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT,(0,0,0,1))
	
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

