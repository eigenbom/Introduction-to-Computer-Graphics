# This Makefile will compile BasicRoom.java
# To run it you will also need to specify the class path
# which is printed to the console upon compilation.
# 
# You will also need to have the jogl dlls in your PATH, e.g.,
# 	set PATH=C:\lib\jogl\lib;%PATH%
# 
# Set JOGLDIR to point to the location of the jogl libraries 
#   (the .jar and .dll files)
#
# Ben Porter, August 2010

# Class path separator, should be a ":" if using linux
CPS = ;

JAVAC = javac
JAVA = java

JOGLDIR = C:\lib\jogl\lib
JOGLLIBS = jogl.all.jar gluegen-rt.jar nativewindow.all.jar
JOGLLIBS_EXP = $(addprefix $(addsuffix \,$(JOGLDIR)),$(JOGLLIBS))

# Build the Class Path
space :=
space +=
JOGLLIBS_LIST = $(subst $(space),$(CPS),$(strip $(JOGLLIBS_EXP)))
CLASSPATH = .$(CPS)$(JOGLLIBS_LIST)

all: BasicRoom

BasicRoom: BasicRoom.java Room.java
	$(JAVAC) -cp $(CLASSPATH) $^
