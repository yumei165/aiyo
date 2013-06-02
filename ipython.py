1, tab completion
2, a? provide information on a
   a?? also include definition of function a if possible
   *a*? provide names matching the string with wildcards
4, Ctrl+C: exit during running a program
5, paste: Ctrl+Shift+V / %paste / %cpaste(use #4 to quit this mode)
6, keyboard shortcuts: Ctrl+U/Ctrl+K <-> Ctrl+y
7, magic commands: 
   %reset -f : force reset
   %automagic : switch if % is needed 
   %magic, %quickref: all magic commands
   %hist: Print command input (and optionally output) history
   %pdb: Automatically enter debugger after any exception
   %paste: Execute pre-formatted Python code from clipboard
   %cpaste: Open a special prompt for manually pasting Python code to be executed
   %reset: Delete all variables / names defined in interactive namespace
   %page: OBJECT Pretty print the object and display it through a pager
   %run script.py: Run a Python script inside IPython
   %prun statement: Execute statement with cProfile and report the profiler output
   %time statement: Report the execution time of single statement
   %timeit statement: Run a statement multiple times to compute an emsemble average execution time. Useful for
                      timing code with very short execution time
   %who, %who_ls, %whos: Display variables defined in interactive namespace, with varying levels of information / verbosity
   %xdel variable: Delete a variable and attempt to clear any references to the object in the IPython internals
   %logstart/%logon/%logoff/%logstate/%logstate
   %alias ll ls -l: ll will mean ls -l(detailed ls)
     %alias test_alias (cd ch08; ls; cd ..): also good for a seq of commands.
   %bookmark db /home/wesm/Dropbox/
     %bookmark -l: display all bookmarks
     #bookmark persists between ipython sessions
   %debug: useful when calling it after an exception is thrown, will start with the error code
   %pdb: debug will be invoked when exception is thrown
   
8, ipython qtconsole --pylab=inline

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img=mpimg.imread('stinkbug.png')
plt.imshow(img)

9, matplotlib integration
$ ipython --pylab: matplotlib plot window will be created automatically; most namespace of numpy/matplotlib will be imported.

10, output/input variables
_/__ : the last/2nd-last output result
_ix: x is the line number, variable name in line x
_x: store the output result for line x

11, Integration with system
!cmd: execute some system cmd
   #get IP address
   ip_info = !ifconfig eth0 | grep "inet "
   ip_info[0].strip()
   
12, ! and $: substitute variable content defined in current envioronment

foo = 'test*'
!ls $foo

13, debugger commands
h: display command list
help cmd: show info of cmd
c: continue program execution
q: quit debugger
b no: set breakpoint line as no in current file.
b filename:no: set breakpoint line as no in filename
s: step into function call
n: execute current line and advance to next line
u/d: move up/down in function call stack
a: show argument for current function
debug statement: Invoke statement statement in new (recursive) debugger
l(ist) statement: Show current position and context at current level of stack
w(here): Print full stack trace with context at current position

 #other ways to use debugger
 def set_trace():
   from IPython.core.debugger import Pdb
   Pdb(color_scheme='Linux').set_trace(sys._getframe().f_back)
 def debug(f, *args, **kwargs):
   from IPython.core.debugger import Pdb
   pdb = Pdb(color_scheme='Linux')
   return pdb.runcall(f, *args, **kwargs)
 #put above codes in profile

14, basic profiling
 #in command line
 python -m cProfile -s cumulative cprof_example.py
   #display execution times of functions in cprof_example.py in sorted order
 #in ipython
 %prun -l 7 -s cumulative run_experiment()
 %run -p -s cumulative cprof_example.py
 #line-by-line profiling: line_profiler library
 %lprun -f func1 -f func2 statement_to_profile
 
15, ipython html notebook
$ ipython notebook --pylab=inline
#cloud notebook

16, module dependency
#modules are loaded only once by default, so if we modified a module imported earlier and want to use the updated:
reload(some_lib)

17, make class friendly
def __repr__(self):
   
18, create multiple profile configurations
ipython profile create secret_project
$ ipython --profile=secret_project

https://notebookcloud.appspot.com/login
 
