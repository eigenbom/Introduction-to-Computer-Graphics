from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import Image
import math

def load_image_and_bind(name):
	im = Image.open(name).transpose(Image.FLIP_TOP_BOTTOM)
	img_data = im.tostring()
	img_size = im.size

	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img_size[0], img_size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

class Enemy(object):
	def __init__(self):
		""" Loads the enemy texture """
		self.tex = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, self.tex)
		load_image_and_bind("figure.png")

		self.pos = (0,0,0)
		self.angle = 0
	
	def set_pos(self, x, y, z):
		self.pos = x,y,z
	
	def set_heading(self, hx, hz):
		# calculate rotation angle
		self.angle = math.degrees(math.atan2(hx,hz))

	def draw(self):
		glPushAttrib(GL_CURRENT_BIT)
		glEnable(GL_TEXTURE_2D)
		glDisable(GL_LIGHTING)
		glBindTexture(GL_TEXTURE_2D, self.tex)

		glTranslatef(self.pos[0],self.pos[1],self.pos[2])
		glRotatef(self.angle,0,1,0)

		h = 10
		w = h/4.

		glBegin(GL_QUADS)
		glTexCoord2f(0,0)
		glVertex3f(-w,0,0)
		glTexCoord2f(1,0)
		glVertex3f(w,0,0)
		glTexCoord2f(1,1)
		glVertex3f(w,h,0)
		glTexCoord2f(0,1)
		glVertex3f(-w,h,0)
		glEnd()

		glDisable(GL_TEXTURE_2D)
		glPopAttrib()



