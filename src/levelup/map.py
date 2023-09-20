 
class map:

    map = []

    def updateMap(x_position, y_position):
        #if valideMove ==true:
            map[character.x_position][character.y_position] = 0
            map[x_position][y_position] = 1

    def generateMap(x_position, y_position):
        self.map = [[0 for i in range(9)] for j in range(9)]
        self.map[x_position][y_position] = 1
        
    def printMap(gameMap):
        print(gameMap)

    



    
