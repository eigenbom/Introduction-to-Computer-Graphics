#
# Demonstrates the different filtering techniques.
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

# filters
NUM_FILTERS = 2
NEAREST, LINEAR = range(NUM_FILTERS)

filterToGL = {NEAREST: GL_NEAREST, LINEAR: GL_LINEAR}
filterToString = {NEAREST: "GL_NEAREST", LINEAR: "GL_LINEAR"}

mini = 0
magni = 0

# images
IMAGES = ["spaghetti.jpg","checks.png"]
IMAGE_POWER_OF_TWO = [False, True]
NUM_IMAGES = len(IMAGES)
image = 0

def load_image_and_bind():
	im = Image.open(IMAGES[image]).transpose(Image.FLIP_TOP_BOTTOM)
	if not IMAGE_POWER_OF_TWO[image]:
		# NOTE: Must be a power of 2, so let's resize it!
		im = im.resize((512,512))

	img_data = im.tostring()
	img_size = im.size

	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img_size[0], img_size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
	update_filters()

def update_filters():	
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, filterToGL[mini])
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, filterToGL[magni])

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()

	glEnable(GL_TEXTURE_2D)

	glPushMatrix()
	
	# rotate around y-axis=0.5
	glTranslatef(.5,.5,0)
	glRotatef(360*0.05*millis/1000.,.3,1,0)
	glScalef(1.0*mouse[0]/width, 1.0*(height-mouse[1])/height, 1)
	glTranslatef(-.5,-.5,0)


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

	glPopMatrix()

	glColor3f(1,1,1)
	glRasterPos2f(0,.2)
	for s in "Minification: " + filterToString[mini]:
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(s))
	glRasterPos2f(0,.1)
	for s in "Magnification: " + filterToString[magni]:
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(s))

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
	global mini, magni, image
	if key=='a':
		mini = (mini + 1)%NUM_FILTERS
	elif key=='z':
		magni = (magni + 1)%NUM_FILTERS
	elif key=='i':
		image = (image + 1)%NUM_IMAGES
		load_image_and_bind()
	else:
		print("a/z to change filters, i to change image")
	update_filters()
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

