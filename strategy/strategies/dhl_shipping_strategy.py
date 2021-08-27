""" Implementation for a dhl shipping strategy """

from strategies.shipping_strategy import ShippingStrategy

class DHLShippingStrategy(ShippingStrategy):
    """ Class for calculating DHL shipping cost """

    def __init__(self) -> None:
        super().__init__()
    
    def calculate(self, order):
        """ calculate shipping cost """
        return 10