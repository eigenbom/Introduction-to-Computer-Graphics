""" 
A general parameter system.

A parameter is a part of a demo. It can be selected, deselected, and be updated.
When a parameter is selected it can be updated.
If it is deselected it remembers its old value.
A parameter has a name and an information tag.
BP 09.09.2010
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Parameter(object):

	def __init__(self, name, info, value, handler):
		self.selected = False
		self.name = name
		self.info = info
		self.value = value
		self.handler = handler

	def select(self):
		self.selected = True

	def deselect(self):
		self.selected = False

	def update(self, event):
		self.value = self.handler(event)


class MouseParameter(Parameter):

	def __init__(self, name, info, value, mouseHandler):
		Parameter.__init__(self,name,info,value,mouseHandler)

class ParameterList(object):

	def __init__(self, parameters):
		self.parameters = parameters
		
		self.parameters[0].select()
		self.selected = 0

	def get(self, name):
		for p in self.parameters:
			if p.name==name: return p
		return None

	def next(self):
		""" Choose the next parameter. """
		self.parameters[self.selected].deselect()
		self.selected = (self.selected + 1)%len(self.parameters)
		self.parameters[self.selected].select()

	def mouseMoved(self, x, y):
		p = self.parameters[self.selected]
		if isinstance(p,MouseParameter):
			p.update((x,y))

	def draw(self,x,y):
		""" Render the list of parameters at coordinates x,y in a (-1,1) ortho proj """
		glPushAttrib(GL_ALL_ATTRIB_BITS)
		glDisable(GL_LIGHTING)
		glDisable(GL_COLOR_MATERIAL)
		glDisable(GL_DEPTH_TEST)

		glMatrixMode(GL_PROJECTION)
		glPushMatrix()
		glLoadIdentity()
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		glLoadIdentity()

		glTranslatef(x,y,0)
		h,dh = 0,0.07
		for p in self.parameters:
			h -= dh
			glPushMatrix()
			if p==self.parameters[self.selected]:
				glColor3f(1,1,1)
			else:
				glColor3f(.4,.4,.4)
			glRasterPos(0,h)
			#print(p.name + ":" + str(glGetFloatv(GL_CURRENT_RASTER_COLOR)[0]))
			pv = str(p.value)
			if (type(p.value)==list or type(p.value)==tuple) and len(p.value)>0 and type(p.value[0])==float:
				pv = ""
				for pe in p.value:
					pv += "%.2f,"%pe

			displayBitmapString(p.name + ":" + pv)
			glPopMatrix()
		
		glMatrixMode(GL_PROJECTION)
		glPopMatrix()
		glMatrixMode(GL_MODELVIEW)
		glPopMatrix()

		glPopAttrib()
	
def displayBitmapString(string):
	for s in string:
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(s))

