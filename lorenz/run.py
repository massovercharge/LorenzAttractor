"""
This file may contain a convenient interface/function for 

1: computing a trajectory using an ODE solver from solver.py
2: save data to file
3: plot data

and possible another function that

2: load data from file
3: plot data

"""

from . import filehandling
from . import plot
from . import solver



def save_case(solver_obj, filename):
    """
    The function 'save_case' takes an object and a filename and writes the
    object to a file in the binary .pk1 format by calling 'write_solver'.
    
    If the supplied object contains an 'euler_path' attribute, plots are
    generated using 'plot2d' and 'plot3d' and written to pdf files using
    'write_plot'.
    
    Parameters:
        solver_obj (lorenz.solver.lorenz_solver): A class object generated
        using the lorenz_solver class.
        filename (str): A file name or path to file without file extension.
    
    Returns:
        None
    
    """
    filehandling.write_solver(solver_obj, filename+'.pk1')
    if hasattr(solver_obj, '_euler_path'):
        filehandling.write_plot(plot.plot2d(solver_obj),
                                filename+'_plot2d.pdf')
        filehandling.write_plot(plot.plot3d(solver_obj),
                                filename+'_plot3d.pdf')
    else:
        print('warning save_case: lorenz_solver object contains no euler_path'+
              ' attribute, plots have not been generated.')
    return

def load_case(filename, return_obj=False):
    """
    The function 'load_case' reads a .pk1 file using 'read_solver'. The content
    of the .pk1 file is expected to contain a single
    lorenz.solver.lorenz_solver object.
    
    If the lorenz.solver.lorenz_solver object has an 'euler_path' attribute the
    euler path is plotted using 'plot2d' and 'plot3d'.
    
    Parameters:
        filename (str): A file name or path to file without file extension.
        return_obj (bool): If True, loaded object is returned (default: False).
    
    Returns:
        lorenz.solver.lorenz_solver: If return_obj=True, a class object.
    
    """
    solver_obj = filehandling.read_solver(filename)

    if hasattr(solver_obj, '_euler_path'):
        plot.plot2d(solver_obj)
        plot.plot3d(solver_obj)
    else:
        print('warning load_case: Unable to generate plots, lorenz_solver '+
                'object with no euler_path attribute')

    if return_obj:
        return solver_obj
    else:
        return
