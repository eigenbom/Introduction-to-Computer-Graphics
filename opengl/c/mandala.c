/* mandala.c - Jon McCormack, April 2005  */

/* Copyright 2005 Jon McCormack
 * Last modified 06 April 2005
 */

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif
#include "bool.h"

#define ROT_INC				0.05		/* how much to rotate each frame */
#define NUM_PRIMS			6
int SQ_F_IDX, SQ_IDX, TRI_F_IDX, TRI_IDX, LINE_IDX;

typedef struct {
	bool	filled;			/* TRUE if prim is filled */
	float	angle;			/* == 360/num */
	float	rad;			/* dist from centre */
	float	sx, sy;			/* scale in x and y */
	float	localRot;		/* local rotation */
	float	col[3];			/* colour */
	int		idx;			/* display list index */
} MandalaPrim;

/*
 * local static variables: g_rotate used to keep track of global rotation
 * g_rotInc is the rotation increment each frame
 *
 */
GLfloat g_rotate = 0;
GLfloat g_rotInc = ROT_INC; /* degree increment for rotation animation */
GLfloat g_localRotInc = -ROT_INC * 4.0;
bool	g_rotateMode = FALSE;
MandalaPrim g_prims[NUM_PRIMS] = {
 { FALSE, 36.0, 5.0, 2.0, 1.0, 0.0, {1.0,0.0,1.0}, 0},
 { TRUE, 10.0, 7.0, 0.5, 1.0, 20.0, {0.0,1.0,1.0}, 0},
 { TRUE, 15.0, 1.0, 1.0, 1.0, 0.0, {0.0,1.0,0.0}, 0},
 { FALSE, 30.0, 1.0, 12.0, 0.5, 0.0, {1.0,1.0,0.0}, 0},
 { TRUE, 90.0, 9.0, 2.0, 2.0, 90.0, {1.0,0.0,0.0}, 0},
 { TRUE, 45.0, 6.0, 2.0, 4.0, -90.0, {0.8,0.8,0.8}, 0}
};

void tagMandalaPrims(){
	g_prims[0].idx = SQ_IDX;
	g_prims[1].idx = SQ_F_IDX;
	g_prims[2].idx = LINE_IDX;
	g_prims[3].idx = TRI_IDX;
	g_prims[4].idx = TRI_F_IDX;
	g_prims[5].idx = TRI_F_IDX;

}

/*
 * drawMandalaPrim
 */
void drawMandalaPrim(MandalaPrim * p) {
	float ang;

	glMatrixMode(GL_MODELVIEW);
	glPushMatrix();
	glRotatef(g_rotate,0.0, 0.0, 1.0); /* mandala rotation */
	for (ang = 0; ang <= 360.0; ang += p->angle) {
		glPushMatrix();
		glRotatef(ang,0.0,0.0,1.0);
		glTranslatef(p->rad,0.0,0.0);		/* move out to radius */
		glRotatef(p->localRot,0.0, 0.0, 1.0);	/* local rotation */
		glScalef(p->sx, p->sy, 1.0);		/* scale */
		glColor3fv(p->col);
		glCallList(p->idx); /* draw primative */
		glPopMatrix();
	}
	glPopMatrix();
}


/*
 * drawSquare
 *
 * Draws a square with size s
 *
 */
void drawSquare(GLfloat size, bool filled) {
	
	size /= 2.0;

	glBegin((filled ? GL_POLYGON : GL_LINE_LOOP));
		glVertex2f(-size, -size);
		glVertex2f(size, -size);
		glVertex2f(size, size);
		glVertex2f(-size, size);
	glEnd();
}

void drawTriangle(GLfloat size, bool filled) {
	size /= 2.0;

	glBegin((filled ? GL_POLYGON : GL_LINE_LOOP));
		glVertex2f(-size, -size);
		glVertex2f(size, -size);
		glVertex2f(0, size);
	glEnd();
}

void drawLine(GLfloat size) {
	size /= 2.0;

	glBegin(GL_LINE);
		glVertex2f(-size, 0);
		glVertex2f(size, 0);
	glEnd();
}
	
	

/*
 * display
 *
 * This function is called by the GLUT to display the graphics
 *
 */
void display(void)
{
	int i;
	GLfloat c; /* used to change color of each star */
	/* set matrix mode to modelview */
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();

  glClear( GL_COLOR_BUFFER_BIT );
	for (i = 0; i < NUM_PRIMS; ++i) {
		drawMandalaPrim(&g_prims[i]);
	}
 	// glFlush(); /* force OpenGL output */
}


/*
 * myReshape
 *
 * This function is called whenever the user (or OS) reshapes the
 * OpenGL window. The GLUT sends the new window dimensions (x,y)
 *
 */
void myReshape(int w, int h)
{
	/* set viewport to new width and height */
	/* note that this command does not change the CTM */
    glViewport(0, 0, w, h);

	/* 
	 * set viewing window in world coordinates 
	 */
    glMatrixMode(GL_PROJECTION); 
    glLoadIdentity(); /* init projection matrix */

    if (w <= h)
        glOrtho(-10.0, 10.0, -10.0 * (GLfloat) h / (GLfloat) w,
            10.0 * (GLfloat) h / (GLfloat) w, -1.0, 1.0);
    else
        glOrtho(-10.0 * (GLfloat) w / (GLfloat) h,
            10.0 * (GLfloat) w / (GLfloat) h, -10.0, 10.0, -1.0, 1.0);

	/* set matrix mode to modelview */
    glMatrixMode(GL_MODELVIEW);
}

/*
 * myKey
 *
 * responds to key presses from the user
 */
void myKey(unsigned char k, int x, int y)
{
	switch (k) {
		case 'q':
		case 'Q':	exit(0);
			break;
		case 'r': g_rotateMode = !g_rotateMode;
			break;
	default:
		printf("Unknown keyboard command \'%c\'.\n", k);
		break;
	}
}


/*
 * myMouse
 *
 * function called by the GLUT when the user presses a mouse button
 *
 * Here we increment the global rotation rate with each press - left to do a
 * positive increment, right for negative, middle to reset
 */
void myMouse(int btn, int state, int x, int y)
{   

    if(btn==GLUT_LEFT_BUTTON && state == GLUT_DOWN)  g_rotInc += ROT_INC;
	if(btn==GLUT_MIDDLE_BUTTON && state == GLUT_DOWN) g_rotInc = ROT_INC;
	if(btn==GLUT_RIGHT_BUTTON && state == GLUT_DOWN) g_rotInc -= ROT_INC;

	/* force redisplay */
	// glutPostRedisplay();
}   

/*
 * myIdleFunc
 *
 * increments the rotation variable within glutMainLoop
 */
void myIdleFunc(void) {

	int i;

	if (g_rotateMode) {
		g_rotate += g_rotInc;
		for (i = 0; i < NUM_PRIMS; ++i)
			g_prims[i].localRot += g_localRotInc;
	}

	/* force glut to call the display function */
	glutPostRedisplay();
}


/*
 * main
 *
 * Initialization and sets graphics callbacks
 *
 */
int main(int argc, char **argv)
{
	/* glutInit MUST be called before any other GLUT/OpenGL calls */
    glutInit(&argc, argv);

	/* need both double buffering and z buffer */

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutCreateWindow("Mandala");

	/* set callback functions */
    glutReshapeFunc(myReshape);
    glutDisplayFunc(display);
	// glutIdleFunc(myIdleFunc);
	glutKeyboardFunc(myKey);
	glutMouseFunc(myMouse);

	/* set clear colour */
	glClearColor(1.0, 1.0, 1.0, 1.0);

	/* set current colour to black */
	glColor3f(0.0, 0.0, 0.0);

	/* create prim display lists */
	int list = glGenLists(5);
	SQ_IDX = list;
	SQ_F_IDX = list+1;
	TRI_IDX = list+2;
	TRI_F_IDX = list+3;
	LINE_IDX = list+4;

	glNewList(SQ_IDX, GL_COMPILE);
		drawSquare(1.0, FALSE);
	glEndList();
	/*
	glNewList(SQ_F_IDX, GL_COMPILE);
		drawSquare(1.0, TRUE);
	glEndList();
	glNewList(TRI_IDX, GL_COMPILE);
		drawTriangle(1.0, FALSE);
	glEndList();
	glNewList(TRI_F_IDX, GL_COMPILE);
		drawTriangle(1.0, TRUE);
	glEndList();
	glNewList(LINE_IDX, GL_COMPILE);
		drawLine(1.0);
	glEndList();
	*/
  tagMandalaPrims();

	glutMainLoop();
	 
	return 0;
}
