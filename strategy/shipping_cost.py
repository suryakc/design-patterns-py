class ShippingCost(object):
    def __init__(self, strategy) -> None:
        super().__init__()
        self._strategy = strategy

    def calculate(self, order):
        return self._strategy.calculate(order)