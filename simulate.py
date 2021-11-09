"""Module that performs the simulation .

Defines a class and relevant functions that provides an interface
to setup up a simulation pass along user inputs etc.
"""

from generate import VisibilityEngine

class Simulator:

    def __init__(self):
        self.array_layout = "inputs/array_layout.txt"
        self.telescope_md = "inputs/telescope_metadata.yaml"
        self.simulation_settings = "inputs/settings.yaml"
        return

    def run(self):
        visibilities = VisibilityEngine(settings_file = self.simulation_settings)
        visibilities.generate()
        return
