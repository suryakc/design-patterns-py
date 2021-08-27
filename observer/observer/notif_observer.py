""" Implementation of Notification Service Observer  """
from observer.observer import Observer

class NotificationSvcObserver(Observer):
    """ An observer for Notification Services """
    def __init__(self) -> None:
        super().__init__()

    def on_order_update(self, order):
        """ Send notifications on order update """
        print("Order updated!")
