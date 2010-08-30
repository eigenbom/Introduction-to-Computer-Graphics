/**
 * Room: A simple room object that draws itself using OpenGL calls.
 *
 * Ben Porter, August 2010
 */

import javax.media.opengl.*;
import javax.media.opengl.glu.*;
import javax.media.opengl.awt.*;
import com.jogamp.opengl.util.*;
import com.jogamp.opengl.util.gl2.GLUT;

/**
 * Room encapsulates the geometry of a room and can draw itself 
 * (using world coordinates).
 *
 * A room is 100x10x100 (x,y,z) with y being the vertical axis.
 * The floor is centered at the world origin.
 * There are some random objects placed in the room.
 *
 * Lighting, depth testing, and color material should be enabled
 * in order to render the room correctly.
 */
public class Room {
	static public final float dx = 100, dy = 10, dz = 100;

	public void draw(GLAutoDrawable drawable){
		GL2 gl = drawable.getGL().getGL2();
		
		float dCol[] = {0,0,0,1,1,1}; // {1,.5f,.5f,1,.2f,.2f};
		
		// Draw the floor
		float coords[] = {-dx/2,-dz/2,dx/2,dz/2};
		float dC[] = {1,1};
		gl.glNormal3f(0,1,0);
		drawCheckeredQuad(gl,coords,-2,0,dC,dCol);
		
		// Draw the ceiling
		gl.glNormal3f(0,-1,0);
		drawCheckeredQuad(gl,coords,1,dy,dC,dCol);

		// Draw the four walls
		// -x,x
		for(int i=0;i<2;i++){
			float c[] = {0,-dz/2,dy,dz/2};
			if (i==0) gl.glNormal3f(1,0,0);
			else gl.glNormal3f(-1,0,0);
			drawCheckeredQuad(gl,c,0-3*i,-dx/2 + dx*i,dC,dCol);
		}
		// -z,z
		for(int i=0;i<2;i++){
			float c[] = {-dx/2,0,dx/2,dy};
			if (i==0) gl.glNormal3f(0,0,1);
			else gl.glNormal3f(0,0,-1);
			drawCheckeredQuad(gl,c,2-3*i,-dz/2 + dz*i,dC,dCol);
		}


		// place some objects in the scene
		// 1. a red teapot at (20,3,20)
		GLUT glut = new GLUT();

		gl.glColor3f(1,0,0);
		gl.glPushMatrix();
		gl.glTranslatef(20,3f,20);
		glut.glutSolidTeapot(4);
		gl.glPopMatrix();

		// 2. A blue sphere at (-20,dy/2,-10)
		gl.glColor3f(0,0,1);
		gl.glPushMatrix();
		gl.glTranslatef(-20,dy/2,-10);
		glut.glutSolidSphere(3,32,32);
		gl.glPopMatrix();

		// 3. A yellow icosahedron at (-5,dy/2,15)
		gl.glColor3f(1,1,0);
		gl.glPushMatrix();
		gl.glTranslatef(-5,dy/2,15);
		gl.glScalef(5,5,5);
		glut.glutSolidIcosahedron();
		gl.glPopMatrix();
	}

	public void drawCheckeredQuad(GL2 gl, float[] coords, int plane, float d, float dC[], float col[]){
		boolean white = false;

		gl.glBegin(GL2.GL_QUADS);
		for(float a=coords[0];a<coords[2];a+=dC[0]){
			white = !white;
			boolean black = !white;

			for(float b=coords[1];b<coords[3];b+=dC[1]){
				black = !black;
				if (black)
					gl.glColor3f(col[0],col[1],col[2]);
				else
					gl.glColor3f(col[3],col[4],col[5]);

				// draw a quad from coord (a,b) to (a+dC[0],b+dC[1])
				// (a,b) map to (x,y,z) based on plane
				if (plane==-2 || plane==1){
					gl.glVertex3f(a,d,b);
					gl.glVertex3f(a+dC[0],d,b);
					gl.glVertex3f(a+dC[0],d,b+dC[1]);
					gl.glVertex3f(a,d,b+dC[1]);					
				}
				else if (plane==0 || plane==-3){
					gl.glVertex3f(d,a,b);
					gl.glVertex3f(d,a,b+dC[1]);
					gl.glVertex3f(d,a+dC[0],b+dC[1]);
					gl.glVertex3f(d,a+dC[0],b);
				}
				else if (plane==2 || plane==-1){
					gl.glVertex3f(a,b,d);
					gl.glVertex3f(a,b+dC[1],d);
					gl.glVertex3f(a+dC[0],b+dC[1],d);
					gl.glVertex3f(a+dC[0],b,d);
				}
			}
		}		
		gl.glEnd();		
	}
}
