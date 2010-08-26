/*
 * BasicCube
 *
 * Simple jogl demo:
 * Displays a cube on the screen that is rotated using mouse movements
 *
 * Ben Porter & Jon McCormack, July 2008
 * Updated August 2010 to be compatible with the latest jogl(JSR-231) by BP
 */

import javax.media.opengl.*;
import javax.media.opengl.glu.*;

import java.awt.*;
import java.awt.event.*;

import javax.media.opengl.awt.*;
import com.jogamp.opengl.util.*;
import com.jogamp.opengl.util.gl2.GLUT;

public class BasicCubeTrace extends Frame implements GLEventListener, MouseMotionListener, WindowListener
{
	static GLU glu;
	static GLUT glut;
	static GLCanvas canvas;

	static int width = 600, height = 600;
	static int[] INSETS = new int[2]; // need this so we can get proper mouse coordinates
	
	int mouseX, mouseY;

	public static void main(String[] args)
	{
		BasicCubeTrace frame = new BasicCubeTrace();
		frame.setSize(width,height);
		frame.setVisible(true);

		INSETS[0] = frame.getInsets().left;
		INSETS[1] = frame.getInsets().top;
	}	

	public BasicCubeTrace()
	{
		/* create default capabilities object. Init options can be set here */
		GLCapabilities capabilities = new GLCapabilities(GLProfile.get(GLProfile.GL2));

		/* create canvas with specified capabilities */
		canvas = new GLCanvas(capabilities);
		canvas.addGLEventListener(this);
		canvas.addMouseMotionListener(this);
		addWindowListener(this);
		add(canvas,BorderLayout.CENTER);
		
		
		glu = new GLU();		// for gluPerspective
		glut = new GLUT();	// for glutCube
	}


	public void init(GLAutoDrawable drawable)
	{
		GL2 gl = drawable.getGL().getGL2();

		gl.glClearColor(1.0f,1.0f,1.0f,1.0f);	// set bg to white
		gl.glEnable(GL2.GL_DEPTH_TEST);			// enable depth buffering
		gl.glEnable(GL2.GL_LIGHTING);			// enable lighting
		gl.glEnable(GL2.GL_LIGHT0);				// use default light
		gl.glEnable(GL2.GL_COLOR_MATERIAL); // use glColor to specify material colour 
		gl.glColorMaterial(GL2.GL_FRONT, GL2.GL_DIFFUSE);
		
		// can choose to run in trace mode or debug mode
		// with something like this...
		canvas.setGL(new TraceGL2(canvas.getGL().getGL2(), System.err));
		// canvas.setGL(new DebugGL2(canvas.getGL()));
	}

	public void reshape(GLAutoDrawable drawable, int x, int y, int w, int h)
	{
		GL2 gl = drawable.getGL().getGL2();
		
		width = w;
		height = h;

		// set correct aspect ratio for perspective projection
		gl.glMatrixMode(GL2.GL_PROJECTION);
		gl.glLoadIdentity();
		glu.gluPerspective(60,1.0*width/height,0.01,20);
	
		// Change mode back to modelview
		gl.glMatrixMode(GL2.GL_MODELVIEW);
		gl.glLoadIdentity();
	}

	public void display(GLAutoDrawable drawable)
	{
		GL2 gl = drawable.getGL().getGL2();
		
		// display callback
		gl.glClear(GL2.GL_COLOR_BUFFER_BIT | GL2.GL_DEPTH_BUFFER_BIT);
		gl.glLoadIdentity();

		glu.gluLookAt(
				1-1.0*mouseY/height,
				2+2*(1-1.0*mouseY/height),
				20.0*(1-1.0*mouseY/height),
				0,0,0,
				0,1,0);

		gl.glColor3f(1.0f,0.0f,0.0f);
		gl.glRotatef(360.0f*mouseX/width,0,1,0);
		glut.glutSolidCube(2.0f);		
	}

	public void dispose(GLAutoDrawable d){}

	public void displayChanged(GLAutoDrawable drawable, boolean modeChanged, boolean deviceChanged)
	{}

	public void mouseMoved(MouseEvent e)
	{
		int x = e.getX();
		int y = e.getY();
		mouseX = x - INSETS[0];
		mouseY = height - y - INSETS[1]; // vertical screencoords flipped
		canvas.repaint();
	}

	public void mouseDragged(MouseEvent e)
	{}
	
	public void windowClosing(WindowEvent e)
	{
		setVisible(false);
		System.exit(0);
	} 
	
	public void windowActivated(WindowEvent e){}
	public void windowClosed(WindowEvent e){}
	public void windowDeactivated(WindowEvent e){}
	public void windowDeiconified(WindowEvent e){}
	public void windowIconified(WindowEvent e){}
	public void windowOpened(WindowEvent e){}
}
