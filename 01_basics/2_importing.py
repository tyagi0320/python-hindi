from intro import chai

chai("ice tea")
#A new folder __pycache__ is created
#Inner working of python:

#1.A byte code(usually hidden) is created for your python code.
#2.This byte code is then fetched by Python VM
#3.Python code is compiled into byte code {bytecode:It is a low level code and is platform independent}
#bytecode runs faster.
#pyc files are compiled bytecode files (frozen binaries) that are generated by the Python interpreter when a Python script is imported or executed. 
#The . pyc files contain compiled bytecode that can be executed directly by the interpreter, without the need to recompile the 
#source code every time the script is run.

#__pycache__:These pyc files a lot of times get deleted,reconstructed forms new versions of itself as per the changes boughtup in code.So to handle 
#all these files in organised way and avoid them getting into main folder a new system folder "__pycache__" is formed which is ultimately useful for python itself.

#the pyc file name "intro-cpython-310.pyc" the 
#first half name: referes to the source change
#second half name: refers to the python version 
#This concept of bytecode files works only for imported flies and not for top level files.

#PVM[Python Virtual Machine]:
#1.It is a software in which a loop is run continously and when a file is fed into the loop
#the execution of that file[byte code files] takes place. 
#2.It is a Run time engine
#3.It is also knows as python interprator.

#note:
#1.Byte code is not a machine code, it is a low level code
#**Machine code: Code which gives instruction to hardware
#2.Byte code is pyhton specific interpretation.
#3.cpython-It is the default pyhton interpretator
#4.Other python interpretators:jython,Ironpython,stackless,PyPy

