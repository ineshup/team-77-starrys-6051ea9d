from unittest import TestCase
from levelup.character import character
from levelup.controller import Direction

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        
        ARBITRARY_NAME = character.name
        testobj = character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def testCharacterMovement(self):

        direction = 'e'
        characterObject = character("testName")
        startingPosition = characterObject.startingPosition
        characterObject.move(Direction.EAST)

        if(direction == 'n'):
            expectedposition = (startingPositon[0], startingPosition[1])
        if(direction =='e'):
            expectedposition = (startingPosition[0]+1, startingPosition[1])
        if(direction =='s'):
            expectedposition = (startingPosition[0], startingPosition[1]+1)
        if(direction=='w'):
            expectedposition = (startingPosition[0] + 1, startingPosition[1])
        
        self.assertEqual(characterObject.currentPosition, expectedposition)

