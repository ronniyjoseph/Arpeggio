"""Module that generates simulated visibilities.

This is currently written around pyuvsim, but would like to generalise to
other simulators

Defines a class and relevant functions that sets up the visibility creation
through pyuvsim, and takes care of all ways we want to peturb the visibilities
"""

import pyuvsim
from .perturbate import ThermalNoise
from .perturbate import AntennaGains

class VisibilityEngine:

    def __init__(self, settings_file):
        self.settings = settings_file
        self.data =  None
        return

    def generate(self):
        self.data = pyuvsim.uvsim.run_uvsim(self.settings, return_uv=True)
        return

    def apply_gains(self):
        gains = AntennaGains()
        self.data = gains.apply(uvdata=self.data)
        return

    def add_noise(self):
        noise = ThermalNoise()
        self.data = noise.apply(uvdata=self.data)
        return
