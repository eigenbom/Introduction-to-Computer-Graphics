from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from camera import *

MS_PER_FRAME = 10
millis = 0

width, height = 900, 300
mouse = [0,0]

cameras = []
camera_select = 0

colours = {"red":(1,0,0),"blue":(0,0,1),"green":(0,1,0),
					"yellow":(1,1,0),"magenta":(1,0,1),"cyan":(0,1,1),
					"white":(1,1,1), "black":(0,0,0)}

# A 1x1x1 Cube centered at [.5,.5,-.5]
class Cube(object):
	vertices = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),
							(0,0,-1),(1,0,-1),(1,1,-1),(0,1,-1)]
	faces = [(0,1,2,3),(1,5,6,2),(4,5,6,7),
					 (4,0,3,7),(4,5,1,0),(3,2,6,7)]
	face_colours = [colours[c] for c in ["red","blue","green","yellow","magenta","cyan"]]
	@staticmethod
	def draw():
		glPushMatrix()
		glTranslatef(-.5,-.5,.5)
		glBegin(GL_QUADS)
		for f in Cube.faces:
			glColor3fv(Cube.face_colours[Cube.faces.index(f)])
			for v in f:
				glVertex3fv(Cube.vertices[v])
		glEnd()
		glPopMatrix()

def draw_axis():
	glBegin(GL_LINES)
	for v in [(1,0,0),(0,1,0),(0,0,1)]:
		glColor3fv(v)
		glVertex3f(0,0,0)
		glVertex3fv(v)
	glEnd()

def display():
	global cameras

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	# render both cameras in separate viewport
	camera = cameras[camera_select]
	#camera.set_fov(120.*mouse[1]/height)

	index = 0
	for v in ((0,0,width/3,height),(width/3,0,width/3,height),(2*width/3,0,width/3,height)):
		apply(glViewport,v)
		camera = cameras[index]
		camera.select(v)
		if index==2:
			for c in cameras:
				if c==camera: continue
				c.render((0,0,width/3,height))
		draw_axis()
		
		# draw 5x5 cubes
		# centered at the origin
		glPushMatrix()
		glTranslatef(-5,0,-5)
		for i in range(5):
			glTranslatef(0,0,2)
			glPushMatrix()
			for j in range(5):
				Cube.draw()
				glTranslatef(2,0,0)
			glPopMatrix()
		glPopMatrix()
		index += 1

	glFlush()

def init():
	global cameras

	camera = PerspectiveCamera(60)
	camera.set_position((20,4,20))
	camera.set_target((0,0,0))
	camera.set_near(10)
	camera.set_far(100)
	camera.set_colour((0,0,1))
	cameras.append(camera)

	camera = PerspectiveCamera(60)
	camera.set_position((20,5,0))
	camera.set_target((0,0,0))
	camera.set_near(15)
	camera.set_far(100)
	camera.set_colour((1,0,0))
	cameras.append(camera)

	camera = PerspectiveCamera(90)
	camera.set_position((0,100,1))
	camera.set_target((0,0,0))
	camera.set_near(80)
	camera.set_far(1000)
	camera.set_colour((1,1,0))
	cameras.append(camera)
	

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
	global cameras	
	
	if (key=='a'): cameras[0].set_fov(cameras[0].fov + 2)
	if (key=='z'): cameras[0].set_fov(cameras[0].fov - 2)
	if (key=='s'): cameras[1].set_fov(cameras[1].fov + 2)
	if (key=='x'): cameras[1].set_fov(cameras[1].fov - 2)

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

