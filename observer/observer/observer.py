""" Define observer """
from abc import ABCMeta, abstractmethod

class Observer(object):
    """ Abstract base class for observers """
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_order_update(self, order):
        """ Order updated """
