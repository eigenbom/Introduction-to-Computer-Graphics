from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from vector import *
import math
from itertools import combinations

class Camera(object):
	""" A virtual camera. """

	def __init__(self):
		self.pos = [0,0,0]
		self.near = .1
		self.far = 100
		self.colour = (1,1,1)

	def set_position(self, pos):
		self.pos = pos

	def set_near(self, near):
		self.near = near

	def set_far(self, far):
		self.far = far

	def set_colour(self, colour):
		self.colour = colour

	def select(self, viewport):
		""" Selects this camera. Sets up the projection and view transforms. 
				viewport specifies the viewport attribs (x,y,w,h)	"""
		pass
	
class PerspectiveCamera(Camera):

	def __init__(self, fov):
		Camera.__init__(self)
		self.fov = fov
		self.target = None

	def set_fov(self, fov):
		self.fov = fov

	def set_target(self, target):
		self.target = target

	def select(self, viewport):
		x,y,w,h = viewport

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(self.fov,1.0*w/h,self.near,self.far)

		if self.target is not None:
			gluLookAt(self.pos[0],self.pos[1],self.pos[2],self.target[0],self.target[1],self.target[2],0,1,0)
		else:
			throw("No target set!")

	def render(self,viewport):
		""" Draws its frustum. """
		glPushMatrix()
		glPushAttrib(GL_ALL_ATTRIB_BITS)
		glColor3fv(self.colour)

		glPushMatrix()
		apply(glTranslatef,self.pos)
		glutSolidSphere(3,32,32)
		glPopMatrix()

		x,y,w,h = viewport
		p = self.pos
		t = self.target
		f = self.far
		n = self.near

		# identify the corner points of the near and far plane and draw lines to them
		near_plane = None #(bottomleft, bottomright, topleft, topright)
		far_plane = None  #same
		
		# up direction = [0,1,0]
		up = [0,1,0]
		forward = self.target[0]-self.pos[0],self.target[1]-self.pos[1],self.target[2]-self.pos[2]
		forward = vect_mult(forward, 1./vect_len(forward))
		# left = up x forward
		left = cross_product(up,forward)
		# now, because up may not be orthogonal to left and forward, we recompute it
		up = cross_product(forward,left)
	
		# far plane		
		# use fov and aspect ratio to compute the dimensions of the far plane
		fh = 2*f*math.tan(math.radians(self.fov/2.0))
		fw = (1.0*w/h)*fh

		# the center of the far plane
		cofp = vect_add(p,vect_mult(forward,f))
		# left*w/2
		lw2 = vect_mult(left,fw/2)
		nlw2 = vect_mult(lw2,-1)
		# up*h/2
		uh2 = vect_mult(up,fh/2)
		nuh2 = vect_mult(uh2,-1)

		# four points on far plane
		lt = vect_add(cofp,vect_add(lw2,uh2))
		rt = vect_add(cofp,vect_add(nlw2,uh2))
		lb = vect_add(cofp,vect_add(lw2,nuh2))
		rb = vect_add(cofp,vect_add(nlw2,nuh2))

		far_plane = (lb,rb,lt,rt)

		# near plane
		nh = 2*n*math.tan(math.radians(self.fov/2.0))
		nw = (1.0*w/h)*nh
		conp = vect_add(p,vect_mult(forward,n))
		lw2 = vect_mult(left,nw/2)
		nlw2 = vect_mult(lw2,-1)
		uh2 = vect_mult(up,nh/2)
		nuh2 = vect_mult(uh2,-1)
		lt = vect_add(conp,vect_add(lw2,uh2))
		rt = vect_add(conp,vect_add(nlw2,uh2))
		lb = vect_add(conp,vect_add(lw2,nuh2))
		rb = vect_add(conp,vect_add(nlw2,nuh2))

		near_plane = (lb,rb,lt,rt)

		# now draw the frustum bounded by these planes

		# draw four outer lines
		glBegin(GL_LINES)
		for cp in zip(near_plane,far_plane):
			glVertex3fv(cp[0])
			glVertex3fv(cp[1])
		glEnd()

		# draw the near and far planes
		lb,rb,lt,rt =  near_plane
		nps = [(lt,rt),(lt,lb),(lb,rb),(rb,rt)]
		lb,rb,lt,rt =  far_plane
		nps.extend([(lt,rt),(lt,lb),(lb,rb),(rb,rt)])

		glBegin(GL_LINES)
		for pairs in nps:
			glVertex3fv(pairs[0])
			glVertex3fv(pairs[1])
		glEnd()

		glPopAttrib()
		glPopMatrix()


