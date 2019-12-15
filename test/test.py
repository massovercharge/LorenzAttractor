"""
In this file you may have your tests


"""
import os
import sys
import unittest
import numpy as np

os.chdir('C:\\Users\\dwp\\OneDrive - Novozymes A S\\PhD\\Kurser\\scipro\\'+
         'project\\lorenz\\test')

sys.path.append(os.path.abspath('../'))

from lorenz import solver
from lorenz import plot
from lorenz import filehandling

class LorenzTest(unittest.TestCase):
    """
    This is a class for testing the Lorenz module.
    
    The module contains test functions for the solver, plot and filehandling.
    
    Attributes:
        None
    """
    def test_solver(self):
        """
        This function runs tests on the solver functionality of the lorenz
        module.        
        """
        # define test parameters for inout / output test of euler() function
        in1 = solver.lorenz_solver(sigma=1,
                                   beta=1,
                                   rho=1,
                                   init=[3,2,1],
                                   N=4,
                                   t=1)
        in1.euler()
        out1 = np.array([[3.,2.,1.], [2.,0.,6.], [0.,-10.,0.],[-10.,0.,0.]])

        # define test parameters for wrong shape of init
        in2 = solver.lorenz_solver(sigma=1,
                                   beta=1,
                                   rho=1,
                                   init=[1,1],
                                   N=1,
                                   t=1)
        out2 = False

        # define test parameters for N=0
        in3 = solver.lorenz_solver(sigma=1,
                                   beta=1,
                                   rho=1,
                                   init=[1,1,1],
                                   N=0,
                                   t=1)
        out3 = False

        # define test parameters for t=0
        in4 = solver.lorenz_solver(sigma=1,
                                   beta=1,
                                   rho=1,
                                   init=[1,1,1],
                                   N=1,
                                   t=0)
        out4 = False

        # define test parameters for floating point error in euler()
        in5 = solver.lorenz_solver(sigma=1,
                                   beta=8/3,
                                   rho=28,
                                   init=[3,2,1],
                                   N=29,
                                   t=0.1)
        out5 = False

        # run the tests
        self.assertEqual(in1.euler_path.tolist(), out1.tolist())
        self.assertEqual(in2.euler(), out2)
        self.assertEqual(in3.euler(), out3)
        self.assertEqual(in4.euler(), out4)
        self.assertEqual(in5.euler(), out5)

    def test_plot(self):
        """
        This function runs tests on the plot functionality of the lorenz
        module.        
        """
        # define test parameters for missing euler_path attribute in plot
        in1 = solver.lorenz_solver(sigma=10,
                                   beta=8/3,
                                   rho=6,
                                   init=[3,2,1],
                                   N=1000,
                                   t=0.01)
        out1 = False
        # run the tests
        self.assertEqual(plot.plot2d(in1), out1)
        self.assertEqual(plot.plot3d(in1), out1)

    def test_filehandling(self):
        """
        This function runs tests on the filehandling functionality of the
        lorenz module.        
        """
        self.assertEqual(filehandling.read_solver(filename=''), False)

if __name__ == '__main__':
    unittest.main()