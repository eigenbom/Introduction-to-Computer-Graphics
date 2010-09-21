from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL import Image

MS_PER_FRAME = 10
millis = 0

width, height = 600, 600
mouse = [0,0]

img_data = None
img_size = None

def load_image():
	global img_data, img_size
	im = Image.open("spaghetti.jpg").transpose(Image.FLIP_TOP_BOTTOM)
	img_data = im.tostring()
	img_size = im.size
	print(img_size)

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()

	glRasterPos2f(0,0)
	glPixelZoom(5.0*mouse[0]/width,5.0*(height-mouse[1])/height)
	glDrawPixels(img_size[0],img_size[1],GL_RGB,GL_UNSIGNED_BYTE,img_data)

	glFlush()

def init():
	glClearColor(0,0,0,0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,1,0,1)
	glMatrixMode(GL_MODELVIEW)

	load_image()

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

