from unittest import TestCase
from levelup.map import map
from levelup.controller import Direction
from levelup.character import character


class testMap(TestCase):

    def testInit(self):

        numPositions = 100
        testObject = map()
        
        self.assertEqual(numPositions, testObject.getPositions())

    def testCalculatePosition(self):
        direction = 'e'

        characterObject = character("testName")

        startingPosition = characterObject.startingPosition

        characterObject.move(direction)

        if(direction == 'n'):
            expectedposition = (startingPositon[0], startingPosition[1])
        if(direction =='e'):
            expectedposition = (startingPosition[0]+1, startingPosition[1])
        if(direction =='s'):
            expectedposition = (startingPosition[0], startingPosition[1]+1)
        if(direction=='w'):
            expectedposition = (startingPosition[0] + 1, startingPosition[1])
        
        self.assertEqual(characterObject.currentPosition, expectedposition)


