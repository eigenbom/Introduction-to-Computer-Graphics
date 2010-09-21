#
# Demonstrates loading an image
# and binding as a texture
# BP 21.09.2010
#

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL import Image

MS_PER_FRAME = 10
millis = 0

width, height = 600, 600
mouse = [0,0]

def load_image_and_bind():
	global img_data, img_size
	im = Image.open("spaghetti.jpg").transpose(Image.FLIP_TOP_BOTTOM)
	# NOTE: Must be a power of 2, so let's resize it!
	im = im.resize((512,512))

	img_data = im.tostring()
	img_size = im.size

	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img_size[0], img_size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)	

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()

	glEnable(GL_TEXTURE_2D)
	
	# rotate around y-axis=0.5
	glTranslatef(.5,0,0)
	glRotatef(360*0.1*millis/1000.,0,1,0)
	glTranslatef(-.5,0,0)

	glBegin(GL_QUADS)
	glTexCoord2f(0,0)
	glVertex3f(0,0,0)
	glTexCoord2f(1,0)
	glVertex3f(1,0,0)
	glTexCoord2f(1,1)
	glVertex3f(1,1,0)
	glTexCoord2f(0,1)
	glVertex3f(0,1,0)
	glEnd()

	glFlush()

def init():
	glClearColor(0,0,0,0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,1,0,1)
	glMatrixMode(GL_MODELVIEW)

	load_image_and_bind()

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

