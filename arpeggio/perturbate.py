"""Module contains various sources of noise .

Defines a class and relevant functions that provides an interface
to perturb idealised cases etc.
"""
import numpy as np
from scipy.constants import Boltzmann as k_B



class ThermalNoise:

    def __init__(self, uvdata=None, T_sys=30, channel_width=390e3, t_integrate=10, A_eff=np.pi*6**2, freqs=1e9):
        # Initialize ThermalNoise object with user defined parameters
        #TODO use pyvudata to fill in some parameters?
        #TODO add in astropy units??
        #TODO add frequency dependent Tsys
        #TODO add frequency dependent Aeff/option to compute Aeff from beam sims

        self.t_integrate = t_integrate
        self.T_sys = T_sys
        self.channel_width = channel_width
        self.A_eff = A_eff
        self.freqs =  freqs
        return

    def temperature(self):
        #computes noise in temperature units [K]
        T_noise = self.T_sys /(np.sqrt(self.channel_width * self.t_integrate))
        return T_noise

    def visibility(self):
        #computes noise in visibility units [Jy]
        v_noise = np.sqrt(2.)*k_B*self.temperature()/self.A_eff*1e26
        return v_noise

    def apply(self, uvdata):
        shape = uvdata.data_array.shape
        noise_jy = self.visibility()
        noise_realisation = np.random.normal(scale=noise_jy, size=shape) + \
                            1j*np.random.normal(scale=noise_jy, size=shape)
        uvdata.data_array += noise_realisation
        return uvdata

class AntennaGains:
    def __init__(self):
        return

class PositionOffsets:
    def __init__(self):
        return

class BeamVariations:
    def __init__(self):
        return

