#
# Demonstrates the use of the accumulation buffer
# BP 21.09.2010
#

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL import Image

width, height = 600, 600
mouse = [0,0]
MS_PER_FRAME = 10
millis = 0
from geometry import *

monkey = None # GeometricModel

accum = False

def toggle_accum():
	global accum
	accum = not accum

def load_image_and_bind():
	global img_data, img_size
	im = Image.open("sphere_map.jpg").transpose(Image.FLIP_TOP_BOTTOM)
	# NOTE: Is already a a power of 2
	# im = im.resize((512,512))

	img_data = im.tostring()
	img_size = im.size

	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img_size[0], img_size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

	glTexGenfv(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
	glTexGenfv(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)

	glEnable(GL_TEXTURE_2D)
	glEnable(GL_TEXTURE_GEN_S)
	glEnable(GL_TEXTURE_GEN_T)

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	# render scene
	
	gluLookAt(1.5,1.5,1.3,0,0,0,0,1,0)
	glColor3f(1,1,1)	
	glRotatef(3*360.*mouse[0]/width,0,1,0)
	glRotatef(2*360.*mouse[1]/height,1,0,0)

	monkey.draw()

	if accum:
		# add results into accum and multiply by some small amount 
		glAccum(GL_ACCUM, .05)
		glAccum(GL_MULT, .95)
	
		# read accumulation buffer back into colour buffer
		glAccum(GL_RETURN, 1)
	
	glFlush()

def init():
	global monkey
	monkey = ObjFile('monkey.obj').get_geometry()

	glClearColor(0,0,0,0)

	glEnable(GL_DEPTH_TEST)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60,1,0.1,10)
	glMatrixMode(GL_MODELVIEW)

	load_image_and_bind()

	glClearAccum(0,0,0,1)
	glClear(GL_ACCUM_BUFFER_BIT)

def timer(i):
	global millis
	millis += MS_PER_FRAME
	glutPostRedisplay()
	glutTimerFunc(MS_PER_FRAME,timer,0)


def resize(w,h):
	global width, height
	width, height = w,h
	glViewport(0,0,w,h)
	glutPostRedisplay()

def motion(x,y):
	global mouse
	mouse = x,y
	glutPostRedisplay()

def key(key,x,y):
	toggle_accum()
	glutPostRedisplay()

if __name__=="__main__":
	glutInit()
	glutInitWindowSize(width,height)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH | GLUT_ACCUM)
	glutCreateWindow("shiny monkey time!")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutKeyboardFunc(key)
	glutTimerFunc(MS_PER_FRAME,timer,0)
	glutMainLoop()

