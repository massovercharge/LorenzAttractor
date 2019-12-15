"""
This file can contain functionalities for saving/loading data

"""

import pickle
import matplotlib.pyplot as plt


def write_solver(solver_obj, filename):
    """
    This function writes an input to a binary file.

    Parameters:
        solver_obj (lorenz.solver.lorenz_solver): A class object generated
        using the lorenz_solver class.
        filename (str): A file name or path to file including file extension.

    Returns:
        None
    """
    file = open(filename, 'wb')
    pickle.dump(solver_obj, file)
    file.flush()
    file.close()

def write_plot(plot, filename):
    """
    This function writes a plot object to a file.

    Parameters:
        plot (matplotlib.figure.Figure): A plot object.
        filename (str): A file name or path to file including file extension.

    Returns:
        None
    """
    plt.tight_layout()
    plt.savefig(filename)
    plt.close(plot)

def read_solver(filename):
    """
    This function reads a .pk1 file.

    Parameters:
        filename (str): A file name or path to file excluding file extension.

    Returns:
        Content of the loaded .pk1 file.
    """
    try:
        file = open(filename+'.pk1', 'rb')
    except IOError:
        print('unable to open file')
        return False
    else:
        solver_obj = pickle.load(file)
        file.close()
        return solver_obj
