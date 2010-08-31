#
# FIT3088: Assignment 2
# An example of hard-coding the building complex
# and then generating the geometry to use in 
# rendering.
#
# Ben Porter, August 2010
#

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Complex(object):

	def __init__(self):
		""" Initialise the complex with hard-coded wall information """
		
		# wall_data is a readable version of the wall positions
		# an "X" marks a wall and a "." marks an empty spot
		wall_data = ["XXXXXXXXXXXXXXXX",
								 "X....XXXXXXXXXXX",
								 "X....X.........X",
								 "X....X.........X",
								 "X....XXXX..XXXXX",
								 "X..............X",
								 "X..............X",
								 "XXXXXXXXXXXXXXXX"];

		# convert the wall_data into a 2d array of booleans
		self.walls = [[True if x=="X" else False for x in row] for row in wall_data]
		
		# the i coord maps to columns and the x world coordinate
		# the j coord maps to rows and the z world coordinate
		# the top right corner maps to (0,0) in world coordinates

		# self.dim = (size in i coord, size in j coord)
		self.dim = (len(self.walls[0]),len(self.walls))
		
		# the width of a single block in world coordinates
		self.dWall = 10
		self.width = self.dWall*self.dim[0]
		self.length = self.dWall*self.dim[1]

		# the height of the complex
		self.height = 20

		# the starting position of the player
		self.starting_position = (3*self.dWall,0,3*self.dWall) 

	def draw(self):
		""" Draw the entire complex. """
		glPushAttrib(GL_ALL_ATTRIB_BITS)

		# draw the floor with quad segments of width dWall
		# alternate the floor tile colours
		glNormal3f(0,1,0)
		glBegin(GL_QUADS)
		for i in range(self.dim[0]):
			for j in range(self.dim[1]):
				if ((i+j)%2==0):
					glColor3f(.9,.9,.9)
				else:
					glColor3f(.2,.2,.2)
				glVertex3f(i*self.dWall,0,j*self.dWall)
				glVertex3f(i*self.dWall,0,(j+1)*self.dWall)
				glVertex3f((1+i)*self.dWall,0,(j+1)*self.dWall)
				glVertex3f((1+i)*self.dWall,0,j*self.dWall)
		glEnd()

		# ceiling
		#glColor3f(1,0,0)
		#glNormal3f(0,-1,0)
		#glBegin(GL_QUADS)
		#glVertex3f(self.width,self.height,0)
		#glVertex3f(self.width,self.height,self.length)
		#glVertex3f(0,self.height,self.length)
		#glVertex3f(0,self.height,0)
		#glEnd()
		
		# draw the walls
		glColor3f(.7,.7,.7)
		for i in range(self.dim[0]):
			for j in range(self.dim[1]):
				if self.walls[j][i]: 
					self.draw_box(i*self.dWall,0,j*self.dWall,self.dWall,self.height,self.dWall)

		glPopAttrib()
	
	def draw_box(self,x,y,z,dx,dy,dz):
		glPushMatrix()
		glTranslatef(x,y,z)
		glScalef(dx,dy,dz)
		glTranslatef(0,.5,0)
		glutSolidCube(1)
		glPopMatrix()

