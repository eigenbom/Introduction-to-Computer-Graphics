from OpenGL.GL import *
from random import random

class GeometricModel(object):
	""" A geometric model that can render itself in OpenGL. """

	def __init__(self):
		self.vertices = []
		self.faces = []
		self.colours = []
		self.normals = None

	def draw(self):
		glBegin(GL_QUADS)
		for f in self.faces:
			if len(f)==4:
				glColor3fv(self.colours[self.faces.index(f)])
				for v in f:	
					glVertex3fv(self.vertices[v])
		glEnd()
		glBegin(GL_TRIANGLES)
		for f in self.faces:
			if len(f)==3:
				glColor3fv(self.colours[self.faces.index(f)])
				for v in f:	
					glVertex3fv(self.vertices[v])
		glEnd()


class ObjFile(object):
	""" (Stupidly) reads in an .obj file and stores it in a geometry object. """

	def __init__(self, name):
		self.file = open(name,'r')

	def get_geometry(self, randomise_face_colours=True):
		""" Get the geometric model described by this file. """
		vertices = []
		faces = []
		colours = []

		for line in self.file.readlines():
			split = line.split()
			if split[0]=='v':
				vertices.append(tuple(float(c) for c in split[1:]))
			elif split[0]=='f':
				faces.append(tuple(int(c)-1 for c in split[1:]))
				if randomise_face_colours:
					colours.append((random(),random(),random()))
		
		g = GeometricModel()
		g.vertices = vertices
		g.faces = faces
		if len(colours)>0:
			g.colours = colours
		return g
