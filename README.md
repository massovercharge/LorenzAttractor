# Implementation of the Lorenz Attractor in python

The following paragraphs will give an introduction into
the programme context.

- Author: Daniel Tandrup Weltz Wollenberg

- This program implements the Lorenz Attractor in python 3.7.4. 
The model consists of three coupled first order ordinary
differential equations which has been implemented using
a simple Euler approach.

## Files and dir structure
```bash
lorenz
│   README.md
│
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
│   │   │   case1.pk1
│   │   │   case1_plot2d.pdf
│   │   │   case1_plot3d.pdf
│   │
│   └───case2
│   │   │   case2.pk1
│   │   │   case2_plot2d.pdf
│   │   │   case2_plot3d.pdf
│   │
│   └───case3
│   │   │   case3.pk1
│   │   │   case3_plot2d.pdf
│   │   │   case3_plot3d.pdf
│   │
│   └───case4
│   │   │   case4.pk1
│   │   │   case4_plot2d.pdf
│   │   │   case4_plot3d.pdf
│   │
│   └───case5
│       │   case5.pk1
│       │   case5_plot2d.pdf
│       │   case5_plot3d.pdf
│
└───test
    │   test.py
```

## The program
### The functions
#### The solver (solver.py)
The program is build up around the lorenz_solver class contained in the 
solver.py file. This class has attributes for all the parameters that are
needed in the 'euler' solver function. The parameters are supplied to the
class when it is initiated. The trajectory (euler_path) can then be calculated
by using the euler() class method on the lorenz_solver class object.
The lorenz_solver class is constructed using properties, this was done
in order to delete any euler_path from the class object if a new value is
assigned to any parameter in the object. In this way an euler_path is always
associated with the parameters that generated it.

#### The plot functions (plot.py)
The plot functions are able to generate 2d projections and a 3d projection
of a trajectory when a lorenz_solver class object is supplied.

The color of the plotted trajectory indicates relative euclidean distance
between the current and previous timepoint.

#### The filehandling functions (filehandling.py)
The file saving functionality is implemented in write_solver and write_plot
which writed the lorenz_solver class object and plots to file respectively.

The loading functionality is implemented in the read_solver function. It
reads the saved lorenz_solver class object.

#### The run functions (run.py)
The run.py file contains master functions which brings together functionality
from the other functions.

The save_case function:
- Saves a lorenz_solver class object to file.
- Generates plots based on the supplied object.
- Saves these plots to file.

The load_case function:
- Loads a lorenz_solver object from file.
- Consttucts the 2d and 3d plots from this object and prints these to the console.
- If the return_obj is set to True, load_case also returns the loaded object.

### Testing the program
The './test/test.py' file contains the nessesary code to run basic tests of the
program using unittest. To run the tests use: '$cd test $python test.py'.
Tests include:
- For the solver:
	- Test a minimal working example for the euler solver.
	- Test case for only two initial corrdinates are supplied to the solver.
	- Test case with number of time steps N=0.
	- Test case with time step size t=0.
	- Test case if input parameters result in floating point error while calculating
	a trajectory.
- For the plot functions:
	- Test case if the supplied lorenz_solver class object is missing the euler_path
	attribute (plot2d).
	- Test case if the supplied lorenz_solver class object is missing the euler_path
	attribute (plot3d).
- For the filehandling functions:
	- Test case for missing file to read_solver function.


The plotting functions are the most time consuming part of the code. Running
the plot2d function for an instance of testcase 1 with 10.000 iterations took 
around 1 second and for the plot3d it was around 0.6 seconds. For the same instance
approx. 0.1 seconds was spend on initiation of the class object and calculation of the
trajectory.

### The test cases

- The program contains 5 test cases with predefined parameters,
running these cases will generate data file and pdf plots in the
results directory with a folder for each case, eg. './results/case1/'. 
To run case 1 use: '$cd cases $python testcase1.py'
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



# 
