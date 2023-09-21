from unittest import TestCase
from levelup.map import map


class testMap(TestCase):

    def testInit():
        testObject = map()
        
        self.aseertEqual((9,9), map.dimensions())


