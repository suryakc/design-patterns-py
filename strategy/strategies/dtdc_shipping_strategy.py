""" Implementation for a dtdc shipping strategy """

from strategies.shipping_strategy import ShippingStrategy

class DTDCShippingStrategy(ShippingStrategy):
    """ Class for calculating DTDC shipping cost """

    def __init__(self) -> None:
        super().__init__()
    
    def calculate(self, order):
        """ calculate shipping cost """
        return 14