""" Defines an abstract base class for all shipping strategies """
from abc import ABCMeta, abstractmethod

class ShippingStrategy(object):
    """ Abstract base class for shipping cost strategies"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, order):
        """ calculate shipping cost """