class TestDivide(TestCase):
    def test_divide(self):
        # Обычное деление
        self.assertEqual(divide(4, 2), 2)
        # Деление с минусом(первое число)
        self.assertEqual(divide(-4, 2), -2)
        # Деление с минусом(второе число)
        self.assertEqual(divide(4, -2), -2)
        # Деление с минусом(оба числа)
        self.assertEqual(divide(-4, -2), 2)
        # Деление(float на int)
        self.assertEqual(divide(4.0, 2), 2.0)
        # Деление(int на float)
        self.assertEqual(divide(4, 2.0), 2.0)
        # Деление(float на float)
        self.assertEqual(divide(4.0, 2.0), 2.0)
        # Большое число делить на малое
        self.assertEqual(divide(4444444444444444444444, 2), 2.2222222222222222e+21)
        # Малое число делить на большое
        self.assertEqual(divide(4, 222222222222222222), 1.8e-17)
        # Большое делить на большое
        self.assertEqual(divide(4e+20, 2e+20), 2.0)
        # Бесконечная мантисса
        self.assertEqual(divide(1, 4/11), 2.75)
        # Делить бесконечную мантиссу на число 
        self.assertEqual(divide(4/11, 2), 4/11/2)
        # Деление на ноль
        self.assertEqual(divide(4, 0), "Can't divide by zero")
        # Ноль делить на бесконечную мантиссу
        self.assertEqual(divide(0, 4/11), 0)
        # Ноль делить на ноль
        self.assertEqual(divide(0, 0), 0)