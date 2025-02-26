# File Name : streetlights.py
# Student Name: Dylan Sams
# email:  samsds@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This is a group assignment that has each group member create a class that models something in the real world and does something such as turning on

# Brief Description of what this module does. This module instantiates the class street_lights and defines all functions and methods for said class
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant:


class street_lights(object):
    """
    Models street lights on the UC campus
    """
    def __init__(self, number_of_lights, turn_on_lights):
        """
        constructor
        @param number_of_lights String: The number of street lights
        @param turn_on_lights String: choose to turn on lights
        """
        self.set_number(number_of_lights)
        self.set_lights(turn_on_lights)
    
    def get_number(self):
        """
        @return String: The number of street lights in the current object
        """
        return self.__number
    
    def set_number(self, number_of_lights):
        """
        Assign a value to the number of street lights in the current object
        @param number_of_lights String: The number of street lights to be assigned
        """
        if len(number_of_lights.strip()) == 0 or number_of_lights == None:
            raise Exception("street_lights Class: number of lights must be provided")
        else:
            self.__number = number_of_lights
    
    def get_lights(self):
        """
        @return String: Choice of whether to turn on or not turn on street lights
        """
        return self.__lights
    
    def set_lights(self, turn_on_lights):
        """
        Assign a value of whether or not to turn on the street lights
        @param turn_on_lights String: The choice of whether or not to turn on street lights to be assigned
        """
        if len(turn_on_lights.strip()) == 0 or turn_on_lights == None:
            raise Exception("street_lights Class: choosing to turn on the lights must be provided")
        else:
            self.__lights = turn_on_lights

    def lights_turning_on(self):
        """
        The action of turning on or not turning on the street lights
        """
        self.__lights = self.__lights.lower()
        if self.__lights.strip() == "yes":
            print(self.__number + " lights will be turned on." )
        else:
            print(self.__number + " lights will not be turned on.")
    
    def __str__(self):
        """
        @return String: A human-readable basic representation of the current object
        """
        return f"Number of Lights: {self.__number}, Lights to turn on: {self.__lights}"