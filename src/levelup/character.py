class character:

    name = ""
    currentPosition = (0,0)
    startingPosition = (0,0)

    def move(self,direction):

        if(direction == 'n'):
            self.currentPosition = (self.currentPositon[0], self.currentPosition[1]-1)
        if(direction =='e'):
            self.currentPosition = (self.currentPosition[0] + 1, self.currentPosition[1])
        if(direction =='s'):
            self.currentPosition = (self.currentPosition[0], self.currentPosition[1]+1)
        if(direction=='w'):
            self.currentPosition = (self.currentPosition[0] - 1, self.currentPosition[1])
        

        

    def __init__(self, character_name):
        self.name = character_name

    def getPosition(self):
        self.currentPosition
    def get_name(self):
        return self.name