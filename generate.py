"""Module that generates simulated visibilities.

Defines a class and relevant functions that sets up the visibility creation
through pyuvsim, and takes care of all ways we want to peturb the visibilities
"""

import pyuvsim

class VisibilityEngine:

    def __init__(self, settings_file):
        self.settings = settings_file
        return

    def generate(self):
        pyuvsim.uvsim.run_uvsim(self.settings, return_uv=True)
        return

    def apply_gains(self):
        return

    def add_noise(self):
        return
