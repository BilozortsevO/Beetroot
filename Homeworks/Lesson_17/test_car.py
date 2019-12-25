import unittest
import HW_17_mod

class CarTestCase(unittest.TestCase):

    def setUp(self):
        self.p1_car = HW_17_mod.Car('Toyota', 'Trueno AE86',
                                     1986, 'white')

    def test_acceleration(self):
        self.p1_car.speed = 0
        self.p1_car.acceleration()
        self.assertEqual (self.p1_car.speed, 1)

        self.p1_car.speed = 999999
        self.p1_car.acceleration()
        self.assertEqual (self.p1_car.speed, 200)

    def test_breaking(self):
        self.p1_car.speed = 100
        self.p1_car.breaking()
        self.assertEqual (self.p1_car.speed, 99)

        self.p1_car.speed = -5
        self. p1_car.breaking()
        self.assertEqual (self.p1_car.speed, 0)

    def test_reverse(self):
        self.p1_car.speed = 0
        self.p1_car.reverse()
        self.assertEqual (self.p1_car.speed, -1)

        self.p1_car.speed = -50
        self.p1_car.reverse()
        self.assertEqual (self.p1_car.speed, -30)

    def test_dir_North(self):
        self.direction = ''
        self.p1_car.dir_North()
        self.assertEqual (self.p1_car.direction, 'North')

    def test_dir_South(self):
        self.direction = ''
        self.p1_car.dir_South()
        self.assertEqual (self.p1_car.direction, 'South')

    def test_dir_East(self):
        self.direction = ''
        self.p1_car.dir_East()
        self.assertEqual (self.p1_car.direction, 'East')

    def test_dir_West(self):
        self.direction = ''
        self.p1_car.dir_West()
        self.assertEqual (self.p1_car.direction, 'West')

unittest.main()        
