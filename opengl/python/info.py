from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
resX,resY = (400,300 )

if __name__ == "__main__":
	glutInit([])
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(resX, resY)
	glutInitWindowPosition(0, 0)
	window = glutCreateWindow("hello")

	for name in (GL_VENDOR,GL_RENDERER,GL_SHADING_LANGUAGE_VERSION ,GL_EXTENSIONS):
		print name,glGetString(name)

