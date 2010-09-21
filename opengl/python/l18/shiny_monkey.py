#
# Demonstrates the use of a sphere map.
# BP 21.09.2010
#

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL import Image

width, height = 600, 600
mouse = [0,0]

from geometry import *

monkey = None # GeometricModel

def load_image_and_bind():
	global img_data, img_size
	im = Image.open("sphere_map.jpg").transpose(Image.FLIP_TOP_BOTTOM)
	# NOTE: Is already a a power of 2
	# im = im.resize((512,512))

	img_data = im.tostring()
	img_size = im.size

	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img_size[0], img_size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

	glTexGenfv(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
	glTexGenfv(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)

	glEnable(GL_TEXTURE_2D)
	glEnable(GL_TEXTURE_GEN_S)
	glEnable(GL_TEXTURE_GEN_T)

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	
	gluLookAt(1.5,1.5,1.3,0,0,0,0,1,0)
	glColor3f(1,1,1)	
	glRotatef(3*360.*mouse[0]/width,0,1,0)
	glRotatef(2*360.*mouse[1]/height,1,0,0)

	monkey.draw()

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
	glutCreateWindow("shiny monkey time!")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutMainLoop()

