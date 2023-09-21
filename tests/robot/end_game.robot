*** Settings ***
Documentation     Test end of game. That character should be like \n\n https://raw.githubusercontent.com/level-up-program/python-robot-reference/main/tests/robot/images/gamerErin.png
Test Template     End game
Library           EndGameLibrary.py

*** Test Cases ***      providedCharacterName      characterName      numPositions     startingPositionX    startingPositionY  startingMoveCount
Blank character name    ${EMPTY}                   Character          100              0                    0                  0


*** Keywords ***
End game
    [Arguments]    ${providedCharacterName}  ${characterName}  ${numPositions}  ${EndPositionX}  ${EndPositionY}  ${EndingMoveCount}
    Initialize controller
    Ending X coordinate should be    ${endPositionX}
    Ending Y coordinate should be    ${endPositionY}
    Ending move count should be      ${endMoveCount}

