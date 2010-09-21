"""
Renders a 1x1x1 cube centered at the origin, with the faces oriented outwards. 
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

colours = {"red":(1,0,0),"blue":(0,0,1),"green":(0,1,0),
					"yellow":(1,1,0),"magenta":(1,0,1),"cyan":(0,1,1),
					"white":(1,1,1), "black":(0,0,0)}

# A 1x1x1 tectured Cube centered at [.5,.5,-.5]
class Cube(object):
	vertices = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),
							(0,0,-1),(1,0,-1),(1,1,-1),(0,1,-1)]
	faces = [(0,1,2,3),(1,5,6,2),(4,7,6,5),
					 (4,0,3,7),(4,5,1,0),(3,2,6,7)]
	face_colours = [colours[c] for c in ["red","blue","green","yellow","magenta","cyan"]]
	@staticmethod
	def draw():
		glPushMatrix()
		glTranslatef(-.5,-.5,.5)
		glBegin(GL_QUADS)
		for f in Cube.faces:
			glColor3fv(Cube.face_colours[Cube.faces.index(f)])
			for v,uv in zip(f,[(0,0),(0,1),(1,1),(1,0)]):
				glTexCoord2f(uv[0],uv[1])
				glVertex3fv(Cube.vertices[v])
		glEnd()
		glPopMatrix()

