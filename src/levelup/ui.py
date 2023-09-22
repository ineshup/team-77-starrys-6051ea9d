import logging
from typing import Callable
from levelup.controller import GameController, Direction, InvalidMoveException
from levelup.character import character

VALID_DIRECTIONS = [x.value for x in Direction]

class GameApp:

    controller: GameController

    def __init__(self):
        self.controller = GameController()

    def prompt(self, menu: str, validation_fn: Callable[[str], bool]) -> str:
        while True:
            response = input(f"\n{menu}\n> ")
            if validation_fn(response):
                break
        return response

    def create_character(self):
        character = self.prompt("Enter character name", lambda x: len(x) > 0)
        self.controller.create_character(character)
        #print(character_object.getName())

    def move_loop(self):
        while True:
            response = self.prompt(
                f"Where would you like to go? {VALID_DIRECTIONS}\n(or ctrl+c to quit)",
                lambda x: x in VALID_DIRECTIONS,
            )
            direction = Direction(response)
            try:
                self.controller.move(direction)
            except InvalidMoveException:
                if self.controller.move(direction) == 'n':
                    print(f"Oh no!  Theres a canyon in the way.  You can't got that way!")
                if self.controller.move(direction) == 'e':
                    print(f"Don't go into the cactus forest!  It will hurt.  You can't got that way!")
                if self.controller.move(direction) == 's':
                    print(f"Where did that mountain come from?  We can't go over it.  You can't got that way!")
                if self.controller.move(direction) == 'w':
                    print(f"Oh no!  A river and you can't swim.  You can't got that way!")
            else:
                print(f"You made a move {direction.name}")
                
                #character.set_character_position(direction.name)
                
            print(self.controller.status)

    def start(self):
        self.create_character()
        self.controller.start_game()
        self.move_loop()

    def quit(self):
        print(f"\n\n{self.controller.status}")
