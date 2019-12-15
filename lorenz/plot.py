"""
This file may contain functionalities for plotting

"""

import matplotlib.pyplot as plt
import matplotlib.collections as mcoll
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import numpy as np


def plot2d(solver_obj):
    """
    This function generates 2d projections from a lorenz_solver class object.

    The object needs all parameters and an euler_path attribute for in order
    to plot.The line color indicates relative euclidean distance travelled
    since the last timestep.

    Parameters:
        solver_obj (lorenz.solver.lorenz_solver): A class object generated
        using the lorenz_solver class.

    Returns:
        matplotlib.figure.Figure: A plot object.
    """
    if not hasattr(solver_obj, '_euler_path'):
        print('An euler_path attribute has not been calculated')
        return False

    fig = plt.figure(figsize=(10, 8)) # define the size of the figure in inches

    x = solver_obj.euler_path[:, 0]
    y = solver_obj.euler_path[:, 1]
    z = solver_obj.euler_path[:, 2]

    # make a grid of subplots to contain the 2d projections
    p1 = plt.subplot2grid((2, 2), (1, 0))
    p2 = plt.subplot2grid((2, 2), (0, 0))
    p3 = plt.subplot2grid((2, 2), (0, 1))
    p4 = plt.subplot2grid((2, 2), (1, 1))

    d = np.zeros(len(x))
    col = np.zeros(len(d))
    d[1:] = np.sqrt(((x[1:] - x[:-1])**2 +
                     (y[1:] - y[:-1])**2 +
                     (z[1:] - z[:-1])**2)) # calculate euclidean distance in 3d
    for i in range(0, len(d), 1):
        col[i] = ((d[i] - d.min()) / (d.max() - d.min())) # normalize distance

    plt.sca(p1) # select p1 for plotting

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = mcoll.LineCollection(segments, array=col, cmap='jet',
                              norm=plt.Normalize(0.0, 1.0),
                              linewidth=0.3, alpha=1)
    p1.add_collection(lc)
    plt.colorbar(lc, label='relative euclidean distance')

    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())
    plt.title('2D projection X,Y')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.sca(p2) # select p2 for plotting

    points = np.array([x, z]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = mcoll.LineCollection(segments, array=col, cmap='jet',
                              norm=plt.Normalize(0.0, 1.0),
                              linewidth=0.3, alpha=1)

    p2.add_collection(lc)
    plt.colorbar(lc, label='relative euclidean distance')
    plt.xlim(x.min(), x.max())
    plt.ylim(z.min(), z.max())
    plt.title('2D projection X,Z')
    plt.xlabel('x')
    plt.ylabel('z')

    plt.sca(p3) # select p3 for plotting

    points = np.array([y, z]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = mcoll.LineCollection(segments, array=col, cmap='jet',
                              norm=plt.Normalize(0.0, 1.0),
                              linewidth=0.3, alpha=1)
    p3.add_collection(lc)
    plt.colorbar(lc, label='relative euclidean distance')
    plt.xlim(y.min(), y.max())
    plt.ylim(z.min(), z.max())
    plt.title('2D projection Y,Z')
    plt.xlabel('y')
    plt.ylabel('z')

    plt.sca(p4) # select p4 for plotting

    # printing parameter values to p4
    p4.text(0.5, 0.9, 'Parameters:',
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p4.text(0.5, 0.8, r'$\sigma = {}$'.format(round(solver_obj.sigma, 4)),
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p4.text(0.5, 0.7, r'$\beta = {}$'.format(round(solver_obj.beta, 4)),
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p4.text(0.5, 0.6, r'$\rho = {}$'.format(round(solver_obj.rho, 4)),
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p4.text(0.5, 0.5, r'$init = {}$'.format(solver_obj.init),
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p4.text(0.5, 0.4, r'$N (steps) = {}$'.format(solver_obj.N),
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p4.text(0.5, 0.3, r'$t (stepzise) = {}$'.format(round(solver_obj.t, 4)),
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p4.get_xaxis().set_visible(False) # hide x axis
    p4.get_yaxis().set_visible(False) # hide y axis


    return fig

def plot3d(solver_obj):
    """
    This function generates a 3d projection from a lorenz_solver class object.

    The object needs all parameters and an euler_path attribute for in order
    to plot. The line color indicates relative euclidean distance travelled
    since the last timestep.

    Parameters:
        solver_obj (lorenz.solver.lorenz_solver): A class object generated
        using the lorenz_solver class.

    Returns:
        matplotlib.figure.Figure: A plot object.
    """
    if not hasattr(solver_obj, '_euler_path'):
        print('An euler_path attribute has not been calculated')
        return False

    x = solver_obj.euler_path[:, 0]
    y = solver_obj.euler_path[:, 1]
    z = solver_obj.euler_path[:, 2]

    fig = plt.figure(figsize=(15, 8))

    p1 = plt.subplot2grid((1, 6), (0, 0), colspan=4, projection='3d')
    p2 = plt.subplot2grid((1, 6), (0, 4), colspan=2)

    plt.sca(p1) # select p1 for plotting
    d = np.zeros(len(x))
    col = np.zeros(len(d))
    d[1:] = np.sqrt(((x[1:] - x[:-1])**2 +
                     (y[1:] - y[:-1])**2 +
                     (z[1:] - z[:-1])**2)) # calculate euclidean distance in 3d
    for i in range(0, len(d), 1):
        col[i] = ((d[i] - d.min()) / (d.max() - d.min())) # normalize distance


    points = np.array([x, y, z]).T.reshape(-1, 1, 3)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = Line3DCollection(segments, array=col, cmap='jet',
                          norm=plt.Normalize(0.0, 1.0),
                          linewidth=0.3, alpha=1)

    p1.add_collection3d(lc)
    fig.colorbar(lc, label='relative euclidean distance', shrink=0.5)
    p1.set_title('3D plot for Lorenz attractor')
    p1.set_xlabel('x')
    p1.set_ylabel('y')
    p1.set_zlabel('z')
    p1.set_xlim(x.min(), x.max())
    p1.set_ylim(y.min(), y.max())
    p1.set_zlim(z.min(), z.max())

    plt.sca(p2) # select p2 for plotting

    # printing parameter values to p4
    p2.text(0.5, 0.9, 'Parameters:',
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p2.text(0.5, 0.8, r'$\sigma = {}$'.format(round(solver_obj.sigma, 4)),
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p2.text(0.5, 0.7, r'$\beta = {}$'.format(round(solver_obj.beta, 4)),
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p2.text(0.5, 0.6, r'$\rho = {}$'.format(round(solver_obj.rho, 4)),
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p2.text(0.5, 0.5, r'$init = {}$'.format(solver_obj.init),
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p2.text(0.5, 0.4, r'$N (steps) = {}$'.format(solver_obj.N),
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p2.text(0.5, 0.3, r'$t (stepzise) = {}$'.format(round(solver_obj.t, 4)),
            verticalalignment='top', horizontalalignment='center', fontsize=12)
    p2.get_xaxis().set_visible(False) # hide x axis
    p2.get_yaxis().set_visible(False) # hide y axis

    return fig
