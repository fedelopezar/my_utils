""" 
BASIC ORBIT PARAMETERS
Just a bunch of functions for quick annalysis of orbit properties.
2019
"""

import numpy as np

class KeplerOrbit():
    """ Gravitational two body problem under the assumptions of point-masses
    and M1 >> M2.
    Arguments:
    M: mass of central object in solar masses
    a: semi-major axis, in the unit system selected
    ecc: (default=0) eccentricity of the orbit
    cgs: (default=False) boolean to set cgs units
    Attributes:
    b: semi-minor axis, in the unit system selected
    p: semi-latus rectum of the curve
    period: orbit period
    frequency: 1/period
    ang_freq: 2 pi / period
    Methods:
    r: distance to source for a given theta
    v_r, v_t: radial and tangential velocities for a given theta
    energy: defines atributes of gravitational, kinetic, and total energy

    """
    def __init__(self, M, a, ecc=0, cgs=False):
        self.cgs = cgs
        if(self.cgs):
            G = 6.674E-8
            Msun = 1.988e33
        else:
            G = 1
            Msun = 1

        self.Msuns = M
        self.M = M * Msun
        self.mu = G * self.M
        self.a = a
        self.ecc = ecc
        self.b = self.a * np.sqrt(1 - self.ecc*self.ecc)
        self.p = self.a * (1 - self.ecc*self.ecc)
        self.period = 2 * np.pi * self.a * np.sqrt(self.a/self.mu)
        self.frequency = 1 / self.period
        self.ang_freq = 2 * np.pi / self.period

    def r(self, theta=0):
        r = self.p / (1 + self.ecc * np.cos(theta))
        return r

    def v_r(self, theta=0):
        v_r = np.sqrt(self.mu/self.p) * self.ecc * np.sin(theta)
        return v_r

    def v_t(self, theta=0):
        v_t = np.sqrt(self.mu/self.p) * (1 + self.ecc * np.cos(theta))
        return v_t

    def energy(self):
        r = self.r()
        v_r = self.v_r()
        v_t = self.v_t()
        self.energy_grav = - self.mu / r
        self.energy_kin = v_r * v_r / 2 + v_t * v_t / 2
        self.energy = self.energy_grav + self.energy_kin
