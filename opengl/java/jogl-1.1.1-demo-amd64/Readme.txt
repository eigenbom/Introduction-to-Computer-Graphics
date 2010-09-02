FIT3088 Example Source for a JOGL-1.1.1 Program.
Ben Porter 02/09/2010
================================================

This directory contains an Eclipse project that has the jogl-1.1.1 libraries. 

It is meant to run under Windows, if you are using linux or OSX then you will need to get the native libs for those OSes.

Instructions
============
After importing this project into Eclipse, select src/BasicRoom.java and then click play. 
A window with an OpenGL rendered room should appear and the mouse should control the camera orientation.

Notes
=====
To setup up a project like this you need a couple of things.

0. Make a new Java Project

1. Then you need to get JOGL version 1.1.1. This can be downloaded at the following address:
   http://download.java.net/media/jogl/builds/archive/jsr-231-1.1.1/jogl-1.1.1-windows-i586.zip
   
   (You may also want to download the JOGL Javadocs:) 
   http://download.java.net/media/jogl/builds/archive/jsr-231-1.1.1/jogl-1.1.1-docs.zip

2. In the jogl-1.1.1-windows-i586.zip file copy all the files in the lib/ directory into the root directory of your project.

3. Next you need to add the two .jars to your class path. You can do this as follows:

	Right-click your project > Properties > Java Build Path > Libraries > Add Jars > Select the two jars in the root dir

4. (Windows only) We need to disable direct draw when we run our app. You can do this as follows:

   When you have written your main .java file, right-click on it > run as > run configurations > arguments > add "-Dsun.java2d.noddraw=true" to the virtual machine arguments
   
   
Troubleshooting
===============

1. I get the error message "Can't load IA 32-bit .dll on a AMD 64-bit platform"

You need to download the other version of the jogl windows library:
http://download.java.net/media/jogl/builds/archive/jsr-231-1.1.1/jogl-1.1.1-windows-amd64.zip