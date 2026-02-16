class TestDivide(TestCase):
    def test_usual_divide(self):
        self.assertEqual(divide(4, 2), 2)

    def test_divide_with_minus(self):
        self.assertEqual(divide(-4, 2), -2)

    def test_divide_with_minus_of_second_value(self):
        self.assertEqual(divide(4, -2), -2)

    def test_divide_with_minus_of_both_value(self):
        self.assertEqual(divide(-4, -2), 2)

    def test_divide_float_int(self):
        self.assertEqual(divide(4.0, 2), 2.0)

    def test_divide_int_float(self):
        self.assertEqual(divide(4, 2.0), 2.0)

    def test_divide_float_float(self):
        self.assertEqual(divide(4.0, 2.0), 2.0)

    def test_divide_inf_mantissa(self):
        self.assertEqual(divide(1, 4/11), 2.75)

    def test_divide_inf_mantissa_int(self):
        self.assertEqual(divide(4/11, 2), 4/11/2)

    def test_divide_big_small(self):
        self.assertEqual(divide(44444444444444444444, 2), 2.2222222222222222e+19)

    def test_divide_small_big(self):
        self.assertEqual(divide(4, 22222222222222222), 1.8e-16)

    def test_divide_big_big(self):
        self.assertEqual(divide(6e+20, 3e+20), 2.0)

    def test_divide_zero(self):
        self.assertEqual(divide(4, 0), "Can't divide by zero")

    def test_divide_zero_zero(self):
        self.assertEqual(divide(0, 0), 0)
        
    def test_divide_zero_inf_mantissa(self):
        self.assertEqual(divide(0, 4/11), 0)

