"""
This demo demonstrates OpenGL lighting.
BP 09.09.2010

"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from parameter import *

width, height = 600, 600
mouse = [0,0]

MS_PER_FRAME = 10
millis = 0

# the mouse coordinates, keys, etc, can modify 
# different parameters of the demo
# to make this easy we need a general parameter system

parameters = ParameterList([
	MouseParameter("Orientation","Modify the teapot orientation.", [0,0], 
		lambda (x,y): (2*360.*x/width,360.*y/height) ),
	MouseParameter("Shininess","Change the material shininess.", 0,
		lambda (x,y): 100.*x/width),
	MouseParameter("Specular", "Change the materials specularity.", (0,0,0,1),
		lambda (x,y): (1.*x/width,1.*x/width,1.*x/width,1)),
	MouseParameter("LightPosition", "Change the light x-z pos.", [2.1,2.3],
		lambda (x,y): (-2+4.*x/width,-2+4.*y/height)),
	MouseParameter("LightDistance", "Change the y-coord of the light.", 2.2,
		lambda (x,y): 20*1.0*(height-y)/height),
])

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	gluLookAt(2,2,2,0,0,0,0,1,0)
	glColor3f(1,1,0)	
	lxz = parameters.get("LightPosition").value
	ly = parameters.get("LightDistance").value
	glLightfv(GL_LIGHT0,GL_POSITION,[lxz[0],ly,lxz[1]])

	glMaterialfv(GL_FRONT, GL_SPECULAR, parameters.get("Specular").value)
	glMaterialf(GL_FRONT, GL_SHININESS, parameters.get("Shininess").value)

	orientation = parameters.get("Orientation").value
	glRotatef(orientation[0],0,1,0)
	glRotatef(orientation[1],1,0,0)
	
	#glRotatef(2*360.*mouse[0]/width,0,1,0)
	#glRotatef(360.*mouse[1]/height,1,0,0)
	glutSolidTeapot(1)

	parameters.draw(-1,-0.5)
	glFlush()

def init():
	glClearColor(0,0,0,0)

	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_COLOR_MATERIAL)
	glColorMaterial(GL_FRONT,GL_DIFFUSE)


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
	global mouse, parameters
	mouse = x, y
	parameters.mouseMoved(x,y)
	glutPostRedisplay()

def timer(i):
	global millis, parameters
	millis += MS_PER_FRAME
	glutPostRedisplay()
	glutTimerFunc(MS_PER_FRAME,timer,0)

def key(key,x,y):
	global parameters
	if key==' ': parameters.next()

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
