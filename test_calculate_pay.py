from unittest import TestCase

from calculate_pay import calculate_pay

class TestCalculatePay(TestCase):
    def test_zero_pay_wage(self):
        self.assertEqual(0, calculate_pay(0, 0))

    def test_calculate_pay(self):
        self.assertEqual(0, calculate_pay(0, 0))

    def test_calculate_pay(self):
        self.assertEqual(0, calculate_pay(0, 0))