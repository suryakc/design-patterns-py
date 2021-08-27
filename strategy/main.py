""" Test the strategies """
from strategies.dhl_shipping_strategy import DHLShippingStrategy
from strategies.dtdc_shipping_strategy import DTDCShippingStrategy
from strategies.fedex_shipping_strategy import FedExShippingStrategy
from shipping_cost import ShippingCost
from order import Order

def test_shipping_costs():
    order = Order(1)
    
    """ DHL """
    dhl_strategy = DHLShippingStrategy()
    shipping_cost = ShippingCost(dhl_strategy)
    assert 10 == shipping_cost.calculate(order)
    
    """ DTDC """
    dtdc_strategy = DTDCShippingStrategy()
    shipping_cost = ShippingCost(dtdc_strategy)
    assert 14 == shipping_cost.calculate(order)

    """ FedEx """
    fedex_strategy = FedExShippingStrategy()
    shipping_cost = ShippingCost(fedex_strategy)
    assert 11 == shipping_cost.calculate(order)

    print("Shipping costs correctly calculated!")

if __name__ == "__main__":
    test_shipping_costs()
