""" Implementation of Notification Service Observer  """
from observer.observer import Observer

class ShippingSvcObserver(Observer):
    """ An observer for Shipping Services """
    def __init__(self) -> None:
        super().__init__()

    def on_order_update(self, order):
        """ Trigger shipping on order ready """
        print("Order shipped!")
