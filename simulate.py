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

        #So what we want to to here
        # a number of different sky realisations
        # a number of antenna position realisations
        # a number of beam realisations
        # a number of thermal noise realisations
        #performance over time sky drifts over

        #Read in a base telescope lay-out
        #Read in base telescope metadata yaml file
        #Create copies
        #Perturb telescope lay-out file, i.e. positions/beam id
        #Pass copies to generate


        return

    def run(self):
        visibilities = VisibilityEngine(settings_file = self.simulation_settings)
        visibilities.generate()
        return
