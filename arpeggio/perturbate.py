"""Module contains various sources of noise .

Defines a class and relevant functions that provides an interface
to perturb idealised cases etc.
"""
import numpy as np
from scipy.constants import Boltzmann as k_B



class ThermalNoise:
    def __init__(self, uvdata=None, T_sys=30, channel_width=40e3, t_integrate=120, A_eff=4**2):
        #TODO figure out from pyvudata what
        #frequency dependence
        #Or take input
        if uvdata != None:
            # Figure things out from pyuvdata object
            self.t_integrate = uvdata.integration_time
        else:
        #user defined path
            self.t_integrate = t_integrate[0]

        #parameters that are not in pyuvobject or not always correct
        #single frequency channel tends to have wrong channel width
        self.T_sys = T_sys
        self.channel_width = channel_width
        self.A_eff = A_eff
        return

    def noise_temperature(self):
        Tnoise = self.T_sys /(np.sqrt(self.channel_width * self.t_integrate))
        return Tnoise

    def add_noise(self, uvdata):
        if self.shape == None:
            pass
        else:
            noise_jy =  2.*k_B*self.noise_temperature(self)/self.A_eff
            noise_realisation = np.random.normal(scale=noise_jy, shape=self.shape) + \
                                1j*np.random.normal(scale=noise_jy, shape=self.shape)
            uvdata.data_array += noise_realisation
        return

class AntennaGains:
    def __init__(self):
        return

class PositionOffsets:
    def __init__(self):
        return

class BeamVariations:
    def __init__(self):
        return

