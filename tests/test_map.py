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
        testingCurrentPosition = [0,0]

        verify = map.verifyBoundary(map, testingCurrentPosition, Direction.EAST)

        self.assertEqual(True, verify)

    def testOutOfMapBoundaries(self):
        testingCurrentPosition = [0,0]

        verify = map.verifyBoundary(map, testingCurrentPosition, Direction.NORTH)

        self.assertEqual(False, verify)