"""
This file could contain the necessary calls to make plots etc for 
case 5

"""
import os
import sys

os.chdir('C:\\Users\\dwp\\OneDrive - Novozymes A S\\PhD\\Kurser\\scipro\\'+
         'project\\lorenz\\cases')

sys.path.append(os.path.abspath('../'))


from lorenz import run
from lorenz import solver

def case5():
    sigma = 14
    beta = 13/3
    rho = 28
    init = [0.1,0.1,1]
    N = 10000
    t = 0.02
    filename = '..\\results\\case5\\case5'

    if not os.path.exists('..\\results\\case5'):
        os.mkdir('..\\results\\case5')

    solver_obj = solver.lorenz_solver(sigma, beta, rho, init, N, t)
    print('Running lorenz solver for case5 given a starting point of '+
          '{}, a stepcount of {} and a stepsize of {}.'.format(init, N, t))
    solver_obj.euler()

    run.save_case(solver_obj, filename)
    print('Loading lorenz_solver class object binary file into variable'+
          ' "case5" and plotting path.')
    case5 = run.load_case(filename=filename)
    return case5

if __name__ == '__main__':
    case5 = case5()