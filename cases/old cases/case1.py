"""
This file could contain the necessary calls to make plots etc for 
case 1

"""
import os
import sys

os.chdir('C:\\Users\\dwp\\OneDrive - Novozymes A S\\PhD\\Kurser\\scipro\\'+
         'project\\lorenz\\cases')

sys.path.append(os.path.abspath('../'))


from lorenz import run
from lorenz import solver

def case1():
    sigma = 10
    beta = 8/3
    rho = 6
    init = [0.1,0.1,0.1]
    N = 10000
    t = 0.02
    filename = '..\\results\\case1\\case1'

    if not os.path.exists('..\\results\\case1'):
        os.mkdir('..\\results\\case1')

    solver_obj = solver.lorenz_solver(sigma, beta, rho, init, N, t)
    print('Running lorenz solver for case1 given a starting point of '+
          '{}, a stepcount of {} and a stepsize of {}.'.format(init, N, t))
    solver_obj.euler()

    run.save_case(solver_obj, filename)
    print('Loading lorenz_solver class object binary file into variable'+
          ' "case1" and plotting path.')
    case1 = run.load_case(filename=filename)
    return case1

if __name__ == '__main__':
    case1 = case1()