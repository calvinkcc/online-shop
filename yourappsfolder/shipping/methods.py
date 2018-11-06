from decimal import Decimal as D

from oscar.apps.shipping import methods
from oscar.core import prices

class NoShippingRequired(methods.Free):
    """
    This is a special shipping method that indicates that no shipping is
    actually required (eg for digital goods).
    """
    code = 'no-shipping-required'
    name = ('Local Pick-Up')

class Standard(methods.Base):
    code = 'standard'
    name = 'Standard shipping'

    charge_per_item = D('0.99')
    threshold = D('12.00')

    def calculate(self, basket):
        # Free for orders over some threshold
        if basket.total_incl_tax > self.threshold:
            return prices.Price(
                currency=basket.currency,
                excl_tax=D('0.00'),
                incl_tax=D('0.00'))

        # Simple method - charge 0.99 per item
        total = basket.num_items * self.charge_per_item
        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)

class UPSStandard(methods.Base):
    code = 'UPSstandard'
    name = 'UPS Standard shipping'

    charge_per_item = D('0.99')
    threshold = D('12.00')

    def calculate(self, basket):
        # Free for orders over some threshold
        if basket.total_incl_tax > self.threshold:
            return prices.Price(
                currency=basket.currency,
                excl_tax=D('0.00'),
                incl_tax=D('0.00'))

        # Simple method - charge 0.99 per item
        total = basket.num_items * self.charge_per_item
        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)


class Express(methods.Base):
    code = 'express'
    name = 'Express shipping'

    charge_per_item = D('1.50')

    def calculate(self, basket):
        total = basket.num_items * self.charge_per_item
        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)