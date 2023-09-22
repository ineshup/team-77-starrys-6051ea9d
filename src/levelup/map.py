 
class map:

    map = [10,10]
    numPositions = 100
    startingPosition = [0,0]

    def getPositions(self):
        return self.numPositions

    def verifyBoundary(self, Position, direction):
        statusMessage = ""
        print("starting position: " + str(Position[0]) + str(Position[1]))
        newPosition = [0,0]

        if(direction == 'n'):
            newPosition[0] = Position[0]
            newPosition[1] = Position[1]-1
        if(direction =='e'):
            newPosition[0] = Position[0] + 1
            newPosition[1] = Position[1]
        if(direction =='s'):
            newPosition[0] = Position[0]
            newPosition[1] = Position[1]+1
        if(direction=='w'):
            newPosition[0] = Position[0] - 1
            newPosition[1] =  Position[1]
        #   
        print("current position: "+ str(newPosition[0]) + str(newPosition[1]))
        if(newPosition[0] >9 or newPosition[0] <0 ):
            return (False)
        
        elif(newPosition[1]>9 or newPosition[1]<0):
            return (False)
        
        return (True)

    def generateMap(self, x_position, y_position):
        self.map = [[0 for i in range(9)] for j in range(9)]
        self.map[x_position][y_position] = 1

    def getMap():
        return self.map
        
    def printMap(self):
        print("map size: " + str(len(self.map)))
        print(self.map)

    



    
