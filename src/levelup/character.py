from random import randrange
class character:

    name = ""
    currentPosition = [0,0]
    startingPosition = [0,0]
    moveCount = 0

    def move(self,direction):

        if(direction == direction.NORTH):
            self.currentPosition = (self.currentPosition[0], self.currentPosition[1]-1)
        if(direction ==direction.EAST):
            self.currentPosition = (self.currentPosition[0] + 1, self.currentPosition[1])
        if(direction ==direction.SOUTH):
            self.currentPosition = (self.currentPosition[0], self.currentPosition[1]+1)
        if(direction== direction.WEST):
            self.currentPosition = (self.currentPosition[0] - 1, self.currentPosition[1])
        
        
    def updateMoveCount(self):
        self.moveCount = self.moveCount + 1

    def __init__(self, character_name):
        self.randomStartingPosition()
        self.name = character_name

    def getPosition(self):
        self.currentPosition
    def get_name(self):
        return self.name 
    def randomStartingPosition(self):
        x = (randrange(10))
        y = (randrange(10))
        self.currentPosition[0] = self.startingPosition[0] = x
        self.currentPosition[1]= self.startingPosition[1] = y     
    #def move_count(self):
    #    x = startingPosition[0]+1    
    #    y = startingPosition[0]+1

