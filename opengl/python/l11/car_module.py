"""
This module offers the Car class, which encapsulates the properties of a car
and provides OpenGL drawing routines to draw it.
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

class Car(object):

	wheel_radius = .5

	def __init__(self, colour=(.5,.5,.5)):
		""" Car constructor """
		self.pos = [0,0,0]
		self.orientation = 0
		self.colour = colour
		self.wheel_rotation = 0
		self.wheel_rotation_speed = None

	def draw(self, wireframe = False):
		""" Draws the car at its current position and orientation """
		glPushMatrix()
		apply(glTranslatef,self.pos)
		glRotatef(self.orientation,0,1,0)
		self._draw_car(wireframe)
		glPopMatrix()

	def set_wheel_rotation(self, rotation):
		""" Sets the rotation amount of the wheels. """
		self.wheel_rotation = rotation

	def set_wheel_rotation_speed(self, rotation_speed):
		""" Sets the rotation speed of the wheel. 0 is no rotation. 1 = 1 rotation per second """
		self.wheel_rotation_speed = rotation_speed

	def set_position(self, pos):
		""" Sets the cars position """
		self.pos = list(pos)

	def update(self, dt):
		""" This routine will move the cars position forward and update its wheel_rotations """
		# to get the change in position, we first get the heading vector from
		# the orientation. the multiply it by an smount proportional to dt 
		# and wheel_rotation
		
		# if the wheels aren't turnin' the car aint movin'
		if self.wheel_rotation_speed is None: return
		else: 
			self.wheel_rotation += 360*(self.wheel_rotation_speed*dt)

		# the heading vector is calculated by taking (0,0,-1) and rotating it
		# by self.orientation degrees. we can't use OPENGL to do this, so have to 
		# do it manually (with trigonometry and stuffs!)
		# ... after some scribbling ...
		theta = math.radians(self.orientation)
		x,z = -math.sin(theta), -math.cos(theta)
		
		# the length of (x,0,z) is 1. 
		# in one full rotation of the wheel the car moves forward by 2PIr units
		# so we want to move forward by: dt*2*PI*r*self.wheel_rotation_speed
		dist = dt*2*math.pi*Car.wheel_radius*self.wheel_rotation_speed
		x,z = x*dist, z*dist
		self.pos[0] += x
		self.pos[2] += z

	def set_orientation(self, orientation):
		""" Sets the cars heading angle. It heads towards -z when orientation=0. """
		self.orientation = orientation

	# routines used by the draw method
	def _draw_wheel(self,wireframe=False):
		""" Draws a wheel of radius 1, centered at the origin, in the x-y plane """
		glPushMatrix()
		glRotatef(-self.wheel_rotation,0,0,1)
		outer_radius = 1
		thickness = .4
		if wireframe:
			glutWireTorus(thickness,outer_radius - thickness,8,8)
		else:
			glutSolidTorus(thickness,outer_radius - thickness,8,8)
			glPushAttrib(GL_CURRENT_BIT)
			glPushAttrib(GL_LIGHTING_BIT)
			glDisable(GL_LIGHTING)
			glColor3f(0,0,0)
			glutWireTorus(thickness+.01,outer_radius - thickness + 0.005,8,8)	
			glPopAttrib()
			glPopAttrib()
		glPopMatrix()

	def _draw_car_body(self,wireframe=False):
		""" Draws the car body. It is a 1x1x2 cube with its base at the origin. """
		# draw the car body	
		glPushMatrix()
		glTranslatef(0,.5,0)
		glScalef(1,1,2)
		if wireframe:
			glutWireCube(1)
		else:
			glutSolidCube(1)
			# draw the wireframe outer shell
			glPushAttrib(GL_CURRENT_BIT)
			glPushAttrib(GL_LIGHTING_BIT)
			glDisable(GL_LIGHTING)
			glColor3f(0,0,0)
			glutWireCube(1.001)	
			glPopAttrib()
			glPopAttrib()
		glPopMatrix()

	def _draw_car(self,wireframe=False):
		""" Draws the untransformed car. """
		wheel_thickness = .4

		glPushMatrix()
		glPushAttrib(GL_CURRENT_BIT)

		# shift the car up so the base lies at the origin
		glTranslatef(0,Car.wheel_radius,0)
		
		glColor3fv(self.colour)
		self._draw_car_body(wireframe)

		# draw the car wheels
		# assume the car is facing down the -z axis
		# front left, front right, back left, back right
		glColor3f(.4,.4,.4)
		ww = wheel_thickness/2
		wheel_centers = [(-.5-ww,0,-1),(.5+ww,0,-1),(-.5-ww,0,1),(.5+ww,0,1)]
		for i in range(4):
			glPushMatrix()
			apply(glTranslatef,wheel_centers[i])
			glRotatef(90,0,1,0)
			glScalef(Car.wheel_radius,Car.wheel_radius,Car.wheel_radius)
			self._draw_wheel(wireframe)
			glPopMatrix()

		glPopAttrib()
		glPopMatrix()

