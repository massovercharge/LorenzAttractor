"""
This file may contain the ODE solver

"""

import numpy as np
np.seterr(over='raise') # raise error for floating-point overflow

class lorenz_solver(object):
    """
    This is a class for managing parameters and calculating trajectories of a
    Lorenz attractor.

    The lorenz_solver class is constructed to associate a calculated trajectory
    with a set of parameters. This means that if the trajectory has already
    been calculated for a given object and a parameter of that object
    is updated, then the trajectory will be deleted from the object.

    Attributes:
        sigma (float): A system parameter, ex 10.
        beta (float): A system parameter, ex 3/8.
        rho (float): A system parameter, ex 6.
        init (list): A set of corrdinates, the starting point for the
        calculation, [x,y,z].
        N (int): Number of steps in the calculation.
        t (float): Stepsize for the calculation.
        euler_path (numpy.ndarray): The x,y,z trajectory returned by euler,
        3 columns and N rows.
    """
    def __init__(self, sigma, beta, rho, init, N=20000, t=0.02):
        """
        The constructor for lorenz_solver class.

        Parameters:
            sigma (float): A system parameter, ex 10.
            beta (float): A system parameter, ex 3/8.
            rho (float): A system parameter, ex 6.
            init (list): A set of coordinates, the starting point for the
            calculation, [x,y,z].
            N (int): Number of steps in the calculation.
            t (float): Stepsize for the calculation.
        """
        self._sigma = sigma
        self._beta = beta
        self._rho = rho
        self._init = init
        self._N = N
        self._t = t

    @property
    def sigma(self):
        """
        A class method to return the current value of the sigma property.

        Parameter:
            self: a lorenz_solver class object.

        Returns:
            float: the current sigma attribute value of self.

        example
            self.sigma
        """
        return self._sigma

    @sigma.setter
    def sigma(self, sigma):
        """
        A class method to update the current value of the sigma property.

        If the lorenz_solver object contains an euler_path attribute when
        the sigma value is updated the euler_path attribute is erased.

        Parameter:
            self: a lorenz_solver class object.
            sigma (float): A system parameter.

        Returns:
            None

        example
            self.sigma = 14
        """
        if sigma != self._sigma:
            print("Updating sigma")
            self._sigma = sigma
            if hasattr(self,'_euler_path'):
                print('Erasing existing trajectory')
                delattr(self, '_euler_path')
        else:
            print("Supplied value is identical to current sigma parameter.")

    @property
    def beta(self):
        """
        A class method to return the current value of the beta property.

        Parameter:
            self: a lorenz_solver class object.

        Returns:
            float: the current sigma attribute value of self.

        example
            self.beta
        """
        return self._beta

    @beta.setter
    def beta(self, beta):
        """
        A class method to update the current value of the beta property.

        If the lorenz_solver object contains an euler_path attribute when
        the beta value is updated the euler_path attribute is erased.

        Parameter:
            self: a lorenz_solver class object.
            beta (float): A system parameter.

        Returns:
            None

        example
            self.beta = 13/3
        """
        if beta != self._beta:
            print("Updating beta")
            self._beta = beta
            if hasattr(self, '_euler_path'):
                print('Erasing existing trajectory')
                delattr(self, '_euler_path')
        else:
            print("Supplied value is identical to current beta parameter.")

    @property
    def rho(self):
        """
        A class method to return the current value of the rho property.

        Parameter:
            self: a lorenz_solver class object.

        Returns:
            float: the current rho attribute value of self.

        example
            self.rho
        """
        return self._rho

    @rho.setter
    def rho(self, rho):
        """
        A class method to update the current value of the rho property.

        If the lorenz_solver object contains an euler_path attribute when
        the rho value is updated the euler_path attribute is erased.

        Parameter:
            self: a lorenz_solver class object.
            rho (float): A system parameter.

        Returns:
            None

        example
            self.rho = 28
        """
        if rho != self._rho:
            print("Updating rho")
            self._rho = rho
            if hasattr(self, '_euler_path'):
                print('Erasing existing trajectory')
                delattr(self, '_euler_path')
        else:
            print("Supplied value is identical to current rho parameter.")

    @property
    def init(self):
        """
        A class method to return the current value of the init property.

        Parameter:
            self: a lorenz_solver class object.

        Returns:
            list: the current init attribute value of self.

        example
            self.init
        """
        return self._init

    @init.setter
    def init(self, init):
        """
        A class method to update the current value of the init property.

        If the lorenz_solver object contains an euler_path attribute when
        the init property is updated the euler_path attribute is erased.

        Parameter:
            self: a lorenz_solver class object.
            init (list): A system parameter.

        Returns:
            None

        example
            self.init = [0.1,0.1,1]
        """
        if not np.shape(init) == (3,):
            print('The shape and format of init should be: [x,y,z]')
            return False
        if init != self._init:
            print("Updating init")
            self._init = init
            if hasattr(self, '_euler_path'):
                print('Erasing existing trajectory')
                delattr(self, '_euler_path')
        else:
            print("Supplied value is identical to current init parameter.")

    @property
    def N(self):
        """
        A class method to return the current value of the N property.

        Parameter:
            self: a lorenz_solver class object.

        Returns:
            int: the current N attribute value of self.

        example
            self.N
        """
        return self._N

    @N.setter
    def N(self, N):
        """
        A class method to update the current value of the N property.

        If the lorenz_solver object contains an euler_path attribute when
        the N value is updated the euler_path attribute is erased.

        Parameter:
            self: a lorenz_solver class object.
            beta (int): A system parameter.

        Returns:
            None

        example
            self.N = 50000
        """
        if N <= 0:
            print('The number of steps (N) cannot be less than 0.')
            return False
        if N != self._N:
            print("Updating N")
            self._N = N
            if hasattr(self, '_euler_path'):
                print('Erasing existing trajectory')
                delattr(self, '_euler_path')
        else:
            print("Supplied value is identical to current N parameter.")

    @property
    def t(self):
        """
        A class method to return the current value of the t property.

        Parameter:
            self: a lorenz_solver class object.

        Returns:
            float: the current t attribute value of self.

        example
            self.t
        """
        return self._t

    @t.setter
    def t(self, t):
        """
        A class method to update the current value of the t property.

        If the lorenz_solver object contains an euler_path attribute when
        the t value is updated the euler_path attribute is erased.

        Parameter:
            self: a lorenz_solver class object.
            t (float): A system parameter.

        Returns:
            None

        example
            self.t = 0.01
        """
        if t <= 0:
            print('The stepsize (t) cannot be less than 0.')
            return False
        if t != self._t:
            print("Updating t")
            self._t = t
            if hasattr(self, '_euler_path'):
                print('Erasing existing trajectory')
                delattr(self, '_euler_path')
        else:
            print("Supplied value is identical to current t parameter.")

    @property
    def euler_path(self):
        """
        A class method to return the current value of the euler_path property.

        Parameter:
            self: a lorenz_solver class object.

        Returns:
            numpy.ndarray: the current N attribute value of self.

        example
            self.euler_path
        """
        if hasattr(self, '_euler_path'):
            return self._euler_path
        else:
            print('An euler_path attribute does not exist for this object.')
            return False

    def euler(self):
        """
        A class method to calculate the trajectory of the Lorenz attractor
        for the given parameter set. The trajectory is added to self as a
        euler_path attribute.

        Parameter:
            self: a lorenz_solver class object.

        Returns:
            None

        example
            self.euler()
        """
        if not np.shape(self._init) == (3,):
            print('The shape and format of init should be: [x,y,z]')
            return False
        if self._N <= 0:
            print('The number of steps (N) cannot be less than 0.')
            return False
        if self._t <= 0:
            print('The stepsize (t) cannot be less than 0.')
            return False
        # initialize array of zeros with shape nrow = N and ncol = 3
        path = np.zeros(shape=(self._N, 3))
        # initialize the path array with the input coordinates from class obj.
        path[0, :] = self._init
        # the solver initiates in the second row of path with first row values
        # as input, i.e. n = 1
        n = 1

        while n < self._N:  # calculate the path over N cycles
            # calculate x coordinate for the n'th step
            try:
                s = self._sigma * (path[n - 1, 1] - path[n - 1, 0])
                path[n, 0] = (s * self._t + path[n - 1, 0])
            except FloatingPointError:
                raise Warning('euler: Floating point error when calculating '+
                              'position in x for step '+
                              '{} out of {} steps'.format(n, self._N))
                return False
            # calculate y coordinate for the n'th step
            try:
                r = self._rho - path[n - 1, 2]

                path[n, 1] = ((path[n - 1, 0] * r - path[n - 1, 1]) * self._t
                              + path[n - 1, 1])
            except FloatingPointError:
                print('euler: Floating point error when calculating '+
                      'position in y for step '+
                      '{} out of {} steps'.format(n, self._N))
                return False
            # calculate z coordinate for the n'th step
            try:
                b = self._beta * path[n - 1, 2]
                path[n, 2] = ((path[n - 1, 0] * path[n - 1, 1] - b) * self._t
                              + path[n - 1, 2])
            except FloatingPointError:
                print('euler: Floating point error when calculating '+
                      'position in z for step '+
                      '{} out of {} steps'.format(n, self._N))
                return False
            n += 1  # increment n by 1

        self._euler_path = path
        return
