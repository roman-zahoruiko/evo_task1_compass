import unittest
from compass.main import direction


class TestCompass(unittest.TestCase):

    def test_compass_cases(self):
        self.assertEqual(direction('S', 180),  'N')
        self.assertEqual(direction('SE', -45), 'E')
        self.assertEqual(direction('W', 495),  'NE')
        self.assertEqual(direction('SE', 315), 'E')
        self.assertEqual(direction('NE', 540), 'SW')
        self.assertEqual(direction('NW', 45), 'N')

    def test_compass_wrong_turn_multiple_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            direction('W', 181)
        self.assertEqual(str(exception_context.exception), 'Turn degree must be a multiple of 45!')

    def test_compass_wrong_turn_value_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            direction("E", -1125)
        self.assertEqual(str(exception_context.exception), 'Turn degree must be between -1080 and 1080!')

    def test_compass_wrong_facing_value_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            direction("Q", 45)
        exception = "Facing must be one of the 8 base directions: N, NE, E, SE, S, SW, W, NW)"
        self.assertEqual(str(exception_context.exception), exception)


if __name__ == '__main__':
    unittest.main()
