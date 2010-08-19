from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

MS_PER_FRAME = 10
millis = 0

width, height = 600, 600
mouse = [0,0]

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

def draw_projection_line(p,q,iters=1000):
	d = q[0]-p[0],q[1]-p[1],q[2]-p[2]
	glBegin(GL_POINTS)
	for i in range(iters):
		di = 1.0*i/iters
		glVertex3f(p[0]+di*d[0],p[1]+di*d[1],p[2]+di*d[2])
	glEnd()

def draw_cube_projection():
	glColor3f(.5,.5,0)
	# first vanishing point
	draw_projection_line((-.5,-.5,-.5),(-.5,-.5,-100))
	draw_projection_line((.5,-.5,-.5),(.5,-.5,-100))
	draw_projection_line((.5,.5,-.5),(.5,.5,-100))
	draw_projection_line((-.5,.5,-.5),(-.5,.5,-100))

	glColor3f(.5,.5,.5)
	#second vanishing point
	draw_projection_line((-.5,-.5,-.5),(-1000,-.5,-.5),iters=3000)
	draw_projection_line((-.5,.5,-.5),(-1000,.5,-.5),iters=3000)
	draw_projection_line((-.5,.5,.5),(-1000,.5,.5),iters=3000)
	draw_projection_line((-.5,-.5,.5),(-1000,-.5,.5),iters=3000)

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	y = 5.0*(1.0*height-mouse[1])/height
	gluLookAt(0,y,3,0,y,0,0,1,0)	
	glRotatef(-90*mouse[0]/width,0,1,0)


	draw_axis()
	draw_cube()
	draw_cube_projection()

	glFlush()

def init():
	glClearColor(0,0,0,0)
	glEnable(GL_DEPTH_TEST)

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

if __name__=="__main__":
	glutInit()
	glutInitWindowSize(width,height)
	glutInitDisplayMode(GLUT_DEPTH)
	glutCreateWindow("cube")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(resize)
	glutPassiveMotionFunc(motion)
	glutTimerFunc(MS_PER_FRAME,timer,0)
	glutMainLoop()

