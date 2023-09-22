*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move N middle of board              5           5               0                     NORTH         5           4           1
Move S middle of board              5           5               1                     SOUTH         5           6           2
Move E middle of board              5           5               2                     EAST          6           5           3
Move W middle of board              5           5               3                     WEST          4           5           4
Move N UpLeft of board              0           0               4                     NORTH         0           0           5
Move S Upleft of board              0           0               5                     SOUTH         0           1           6
Move E Upleft of board              0           0               6                     EAST          1           0           7
Move W Upleft of board              0           0               7                     WEST          0           0           8
Move N UpRight of board             9           0               4                     NORTH         9           0           5
Move S UpRight of board             9           0               5                     SOUTH         9           1           6
Move E UpRight of board             9           0               6                     EAST          9           0           7
Move W UpRight of board             9           0               7                     WEST          8           0           8
Move N DnLeft of board              0           9               4                     NORTH         0           8           5
Move S Dnleft of board              0           9               5                     SOUTH         0           9           6
Move E Dnleft of board              0           9               6                     EAST          1           9           7
Move W Dnleft of board              0           9               7                     WEST          0           9           8
Move N DnRight of board             9           9               4                     NORTH         9           8           5
Move S DnRight of board             9           9               5                     SOUTH         9           9           6
Move E DnRight of board             9           9               6                     EAST          9           9           7
Move W DnRight of board             9           9               7                     WEST          8           9           8


*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${Direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${Direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}