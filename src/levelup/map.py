 
class map:

    map = []
    numPositions = 100
    startingPosition = (0,0)

    def getPositions(self):
        return self.numPositions

    def verifyBoundary(self, position, direction):
        statusMessage = ""
        newPosition = ()
        if(direction == 'n'):
            newPosition = (Positon[0], Position[1]-1)
        if(direction =='e'):
            newPosition = (Position[0] + 1, Position[1])
        if(direction =='s'):
            newPosition = (Position[0], Position[1]+1)
        if(direction=='w'):
            newPosition = (Position[0] - 1, Position[1])
        #   
        if(newPosition[0] >9 or newPosition[0] <0 ):
            return (false)
        
        elif(newPosition[1]>9 or newPosition[1]<0):
            return (false)
        
        return (true)

    def generateMap(self, x_position, y_position):
        self.map = [[0 for i in range(9)] for j in range(9)]
        self.map[x_position][y_position] = 1

    def getMap():
        return self.map
        
    def printMap(self):
        print("map size: " + str(len(self.map)))
        print(self.map)

    



    
