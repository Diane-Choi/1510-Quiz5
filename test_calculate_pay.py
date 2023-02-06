from unittest import TestCase

from calculate_pay import calculate_pay

class TestCalculatePay(TestCase):
    def test_zero_pay_wage(self):
        self.assertEqual(0, calculate_pay(0, 0))

    def test_negative_pay_wage(self):
        self.assertEqual(0, calculate_pay(-99, -99))

    def test_negative_wage_zero_hour(self):
        self.assertEqual(0, calculate_pay(0, -99))

    def test_negative_wage_positive_hour(self):
        self.assertEqual(0, calculate_pay(99, -99))

    def test_zero_wage_positive_hour(self):
         self.assertEqual(0, calculate_pay(99, 0))

    def test_zero_wage_negative_hour(self):
        self.assertEqual(0, calculate_pay(-99, 0))

    def test_positive_wage_positive_hour(self):
         self.assertEqual(2000000, calculate_pay(1000, 1000))

    def test_positive_wage_zero_hour(self):
         self.assertEqual(0, calculate_pay(0, 99))

    def test_positive_wage_negative_hour(self):
         self.assertEqual(0, calculate_pay(-99, 1000))