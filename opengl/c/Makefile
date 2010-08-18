# A simple opengl program
# Windows/MinGW version by Ben Porter 2010

CFLAGS = -g
GLUT_INC = C:\lib\glut\include
GLUT_LIB = C:\lib\glut
GLUT_DEFINES = -D_STDCALL_SUPPORTED -D_M_IX86

simple: simple.c 
	gcc -o simple.exe $(CFLAGS) simple.c -lopengl32 -I$(GLUT_INC) -L$(GLUT_LIB) -lglut32 $(GLUT_DEFINES)

text: text.c
	gcc -o text.exe $(CFLAGS) text.c -lopengl32 -I$(GLUT_INC) -L$(GLUT_LIB) -lglut32 $(GLUT_DEFINES)

mandala: mandala.c
	gcc -o mandala.exe $(CFLAGS) mandala.c -lopengl32 -I$(GLUT_INC) -L$(GLUT_LIB) -lglut32 $(GLUT_DEFINES)
