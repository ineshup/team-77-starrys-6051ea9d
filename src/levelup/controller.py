import logging
from dataclasses import dataclass
from enum import Enum
from levelup.character import character
from levelup.map import map
from levelup.images import images


DEFAULT_CHARACTER_NAME = "Character"

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: tuple = (0,0)
    move_count: int = 0
    

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:


    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def start_game(self, character_object):

        print(images.introTitle())
        print("welcome "+ str(character_object.name) + " to stagecoach robbery!")




        

    # Pre-implemented to demonstrate ATDD
    # TODO: Update this if it does not match your design (hint - it doesnt)
    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.status.character_name = character_name
            character_object = character(character_name)
        else:
            self.status.character_name = DEFAULT_CHARACTER_NAME
        return character_object
    def move(self, character_object, direction: Direction) -> None:
        # TODO: Implement move - should call something on another class
        # TODO: Should probably also update the game results
        print("")
        #see build result

        characterPosition = character_object.currentPosition

        validatedMove = map.verifyBoundary(map, characterPosition, direction)
        character_object.updateMoveCount()
        self.status.move_count = character_object.moveCount
        if(validatedMove == True):
            character_object.move(direction)
            self.status.current_position = character_object.currentPosition
            
        return(validatedMove)


        

    def set_character_position(self, xycoordinates: tuple) -> None:


        # TODO: IMPLEMENT THIS TO SET CHARACTERS CURRENT POSITION -- exists to be testable
        pass

    def set_current_move_count(self, move_count: int) -> None:
        # TODO: IMPLEMENT THIS TO SET CURRENT MOVE COUNT -- exists to be testable
        pass

    def get_total_positions(self) -> int:
        # TODO: IMPLEMENT THIS TO GET THE TOTAL POSITIONS FROM THE MAP - - exists to be
        # testable
        return -10

    
