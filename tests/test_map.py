from unittest import TestCase
from levelup.map import map


class testMap(TestCase):

    def testInit(self):

        numPositions = 100
        testObject = map()
        
        self.assertEqual(numPositions, testObject.getPositions())


