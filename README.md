# 1. PYTHON + SCIENTIFIC COMPUTING, PROJECT
### Implementation of the Lorenz Attractor in python
A repository containing a solution to the exam project for the
PhD course "Scientific Computing using Python, part 1", 
held at Aalborg University, November 2019.

#  
The following paragraphs will give an introduction into
the programme context.

- Author: Daniel Tandrup Weltz Wollenberg

- This program implements the Lorenz Attractor in python 3.7.4. 
The model consists of three coupled first order ordinary
differential equations which has been implemented using
a simple Euler approach.

## Files and dir structure
lorenz  <br />
│   README.md  <br /> 
│  <br />
└───cases
│   │   testcase1.py
│   │   testcase2.py
│   │   testcase3.py
│   │   testcase4.py
│   │   testcase5.py
│   
└───lorenz
│   │   __init__.py
│   │   filehandling.py
│   │   plot.py
│   │   run.py
│   │   solver.py
│   
└───results
│   └───case1
│   └───case2
│   └───case3
│   └───case4
│   └───case5
│   
└───test
    │   test.py

## The program
### The test cases
- The program contains 5 test cases with predefined parameters,
running these cases will generate data file and pdf plots in the
results directory with a filder for each case, eg. './results/case1/'.
case 1 '$cd cases $python case1.py'
	- testcase1 observations: These parameters result in a single spiral
	which is directed inwards to the center. Initially the euclidean distance
	indicate acceleration. But after this initial acceleration phase 
	the euclidean distance traversed per timestep decreases as the trajectory 
	approaches the center of the spiral.
	- testcase2 observations: These parameters form a trajectory which resembles
	a slightly distorded figure-8. The size of each eye in the figure 8 is
	approximately 1/5 the diameter of each of the two discs forming the figure.
	The euclidean distance traveled per timestep seams to derease as the
	trajectory approaches each eye of the figure-8 but begin increasing
	again before returning to the other eye. The closer the trajectory
	gets to each of the centers of the eyes, the smaller the distance travelled 
	per timestep.
	- testcase3 observations: The trajectory formed by these parameters also
	form a distorded figure-8, however this time the eyes are much smaller
	relative to the disc. Again, The closer the trajectory gets to each of 
	the centers of the eyes, the smaller the distance travelled per timestep.
	- testcase4 observations: The trajectory formed by these parameters
	resemble case 2 and 3, this time the diameter of the two eyes are
	roughly 1/4 the diameter of each disc.
	- testcase5 observations: The trajectory formed by these parameters mostly
	resemble testcase3, with narrow eyes. However, the figure-8 seams to cover a
	larger area than testcase3.
### The functions
The functions are documented using docstrings.

# 
you might need to put something like

import sys
sys.path.append('../')
import lorenz

in e.g. cases/case1.py or test/test.py to be access the functions etc.
you make in lorenz/solver.py, lorenz/run.py etc.
