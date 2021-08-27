""" Implementation for a fedex shipping strategy """

from strategies.shipping_strategy import ShippingStrategy

class FedExShippingStrategy(ShippingStrategy):
    """ Class for calculating FedEx shipping cost """

    def __init__(self) -> None:
        super().__init__()
    
    def calculate(self, order):
        """ calculate shipping cost """
        return 11