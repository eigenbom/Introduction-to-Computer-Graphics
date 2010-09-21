from OpenGL.GL import *
from random import random

class GeometricModel(object):
	""" A geometric model that can render itself in OpenGL. """

	def __init__(self):
		self.vertices = []
		self.faces = [] # each face is a 4-tuple with either 1-index or 2
		self.colours = []
		self.normals = []

		self.dl = None

	def draw(self):
		# on the first time around it caches itself in a display list
		if self.dl is None:
			self.dl = glGenLists(1)
			glNewList(self.dl, GL_COMPILE_AND_EXECUTE)
			
			glBegin(GL_QUADS)
			
			draw_normals = False
			if len(self.normals)>0:
				draw_normals = True

			draw_colours = False
			if len(self.colours)>0:
				draw_colours = True

			normals = self.normals if draw_normals else [None]*len(self.faces)
			
			for f in self.faces:
				if len(f)==4:
					if draw_colours: glColor3fv(self.colours[self.faces.index(f)])
					for v in f:	
						if draw_normals:
							glNormal3fv(self.normals[v[1]])
							glVertex3fv(self.vertices[v[0]])
						else:
							glVertex3fv(self.vertices[v])
			glEnd()
			glBegin(GL_TRIANGLES)
			for f in self.faces:
				if len(f)==3:
					if draw_colours: glColor3fv(self.colours[self.faces.index(f)])
					for v in f:	
						if draw_normals:
							glNormal3fv(self.normals[v[1]])
							glVertex3fv(self.vertices[v[0]])
						else:
							glVertex3fv(self.vertices[v])
			glEnd()
			glEndList()
		else:
			glCallList(self.dl)

class ObjFile(object):
	""" (Stupidly) reads in an .obj file and stores it in a geometry object. """

	def __init__(self, name):
		self.file = open(name,'r')

	def get_geometry(self, randomise_face_colours=False, compute_normals=False):
		""" Get the geometric model described by this file. """
		vertices = []
		faces = []
		colours = []
		normals = []

		for line in self.file.readlines():
			split = line.split()
			if split[0]=='v':
				vertices.append(tuple(float(c) for c in split[1:]))
			elif split[0]=='vn':
				normals.append(tuple(float(c) for c in split[1:]))
			elif split[0]=='f':
				pieces = split[1:]
				if '/' in pieces[0]:
					face = []
					for s in pieces:
						bits = s.split('//')
						face.append(tuple(int(c)-1 for c in s.split('//')))
					faces.append(tuple(face))
				else:
					faces.append(tuple(int(c)-1 for c in split[1:]))
				if randomise_face_colours:
					colours.append((random(),random(),random()))
		
		g = GeometricModel()
		g.vertices = vertices
		g.faces = faces
		g.normals = normals
		if len(colours)>0:
			g.colours = colours
		return g
