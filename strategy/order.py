""" Defines an order """

class Order(object):
    """ Implementation of Order """
    def __init__(self, id, order_type = None, order_date = None, address=None):
        self._id = id
        self._order_type = order_type
        self._date = order_date
        self._address = address
    