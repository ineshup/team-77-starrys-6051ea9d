from unittest import TestCase
from levelup.map import map
from levelup.controller import Direction
from levelup.character import character


class testMap(TestCase):

    def testInit(self):

        numPositions = 100
        testObject = map()
        
        self.assertEqual(numPositions, testObject.getPositions())

    def testWithinMapBoundaries(self):
        Direction = 'e'
        testingCurrentPosition = [0,0]

        verify = map.verifyBoundary(map, testingCurrentPosition, Direction)

        self.assertEqual(True, verify)

    def testOutOfMapBoundaries(self):
        Direction = 'n'
        testingCurrentPosition = [0,0]

        verify = map.verifyBoundary(map, testingCurrentPosition, Direction)

        self.assertEqual(False, verify)