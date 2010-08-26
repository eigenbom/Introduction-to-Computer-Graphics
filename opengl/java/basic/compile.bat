set JOGLDIR=C:\lib\jogl\lib

set CLASSPATH=.;%JOGLDIR%\jogl.all.jar;%JOGLDIR%\gluegen-rt.jar;%JOGLDIR%\nativewindow.all.jar
javac BasicCube.java
javac BasicCubeTrace.java

set CLASSPATH=%CLASSPATH%;%JOGLDIR%\newt.all.jar
javac GLInfo.java
