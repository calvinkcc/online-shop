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

class USPSFC(methods.Base):
    code = 'USPSFC'
    name = 'USPS First Class (2-5 Days)'

    threshold = D('100.00')

    def calculate(self, basket):
        # Free for orders over some threshold
        if basket.total_excl_tax > self.threshold:
            return prices.Price(
                currency=basket.currency,
                excl_tax=D('0.00'),
                incl_tax=D('0.00'))

        total = D('5.00')
        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)

class USPSP(methods.Base):
    code = 'USPSP'
    name = 'USPS Priority (2-3 Days)'

    def calculate(self, basket):

        total = D('8.00')
        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)

class USPSE(methods.Base):
    code = 'USPSE'
    name = 'USPS Express (1-2 Days)'


    def calculate(self, basket):

        total = D('32.50')
        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)


class UPSG(methods.Base):
    code = 'UPSG'
    name = 'UPS Ground (1-5 Days)'


    def calculate(self, basket):

        total = D('18.00')
        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)

class FEDEXG(methods.Base):
    code = 'FEDEXG'
    name = 'FedEx Ground (1-5 Days)'


    def calculate(self, basket):

        total = D('18.00')
        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)

class FEDEX2D(methods.Base):
    code = 'FEDEX2DAY'
    name = 'FedEx 2-Day (2 Days)'


    def calculate(self, basket):

        total = D('28.00')
        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)

class FEDEXO(methods.Base):
    code = 'FEDEXO'
    name = 'FedEx Overnight (1 Day)'


    def calculate(self, basket):

        total = D('55.00')
        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)
