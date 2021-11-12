"""Module contains various sources of noise .

Defines classes that apply 'real world' effects to simulated idealized data

"""
import numpy as np
from scipy.constants import Boltzmann as k_B


class AntennaGains:
    """
    This class generates antenna gains, applies them to simulated observations
    and stores them for subsequent evaluations

    """
    def __init__(self, variance=0.1):
        """

        Parameters
        ----------
        variance
        """
        #TODO bandpass implementation
        #TODO dealing with polarization
        self.variance = variance
        self.gains = None
        return

    def apply(self, uvdata):
        #First Create an antenna x frequency map
        #reshape into baseline x frequency map
        #apply to uvdata.
        shape = (uvdata.Nants_data, uvdata.Nfreqs)
        self.gains = np.random.uniform(1, self.variance, size= shape)\
                     +1j*np.random.normal(0, self.variance, size=shape)
        map = uvdata.baseline_to_antnums(uvdata.baseline_array)
        uvdata.data_array[:,0,:,0] *= self.gains[map[0],:]*np.conj(self.gains[map[1],:])
        return uvdata

    def write(self):
        return

class ThermalNoise:
    """
    This class generates thermal noise for simulated observations
    """
    def __init__(self, T_sys=30, channel_width=390e3, t_integrate=10, A_eff=np.pi*6**2, freqs=1e9):
        # Initialize ThermalNoise object with user defined parameters
        #TODO use pyvudata to fill in some parameters?
        #TODO add in astropy units??
        #TODO add frequency dependent Tsys
        #TODO add frequency dependent Aeff/option to compute Aeff from beam sims
        #TODO maybe create general unit conversion functions Jy -> K vice versa

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


class PositionOffsets:
    """
    This class generates positions offsets to idealised antenna positions
    """
    def __init__(self):
        return

class BeamVariations:
    """
    This class adds beam perturbations to idealised beams or deals with shuffles in the
    antenna beam index
    """
    def __init__(self):
        return

