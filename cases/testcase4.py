"""
This file could contain the necessary calls to make plots etc for 
case 4

"""
import os
import sys

os.chdir('C:\\Users\\dwp\\OneDrive - Novozymes A S\\PhD\\Kurser\\scipro\\'+
         'project\\lorenz\\cases')

sys.path.append(os.path.abspath('../'))


from lorenz import run
from lorenz import solver

def case4():
    """
    This function contains the nessesary calls to generate a lorenz_solver
    object and plots for case 4. The function will also save the data and plots
    to files.

    Parameters:
        None

    Returns:
        None
    """
    sigma = 14
    beta = 8/3
    rho = 28
    init = [0.1,0.1,0.1]
    N = 20000
    t = 0.02
    filename = '..\\results\\case4\\case4'

    if not os.path.exists('..\\results\\case4'):
        os.mkdir('..\\results\\case4')

    solver_obj = solver.lorenz_solver(sigma, beta, rho, init, N, t)
    print('Running lorenz solver for case4 given a starting point of '+
          '{}, a stepcount of {} and a stepsize of {}.'.format(init, N, t))
    solver_obj.euler()
    print('Writing lorenz object to binary file and generating pdf plots.')
    run.save_case(solver_obj, filename)
    print('Data and plots are saved to case result directory.')
    return

if __name__ == '__main__':
    case4()