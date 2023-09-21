from unittest import TestCase
from levelup.map import map
from levelup.controller import Direction
from levelup.character import character


class testMap(TestCase):

    def testInit(self):

        numPositions = 100
        testObject = map()
        
        self.assertEqual(numPositions, testObject.getPositions())
<<<<<<< HEAD
=======

    
        
        

>>>>>>> f733da9 (scott understood concept)
