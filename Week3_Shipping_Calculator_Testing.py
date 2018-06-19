import unittest
from Week3_Shipping_Calculator_Project import ground_shipping # from .py import the following function to test


class TestShipping(unittest.TestCase):

    def test_ground_shipping(self):
        weight = 1.0
        cost = ground_shipping(weight)
        self.assertEqual((1.50 * weight) + 20.00, cost)

        weight = 5
        cost = ground_shipping(weight)
        self.assertEqual((3.00 * weight) + 20.00, cost)

        weight = 8
        cost = ground_shipping(weight)
        self.assertEqual((4.00 * weight) + 20.00, cost)

        weight = 11
        cost = ground_shipping(weight)  # Added 10 to cause an error, if you take it away this passes.
        self.assertEqual((4.75 * weight) + 20.00, cost)

unittest.main()
