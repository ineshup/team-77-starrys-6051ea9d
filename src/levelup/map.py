 
class map:

    map = []
    dimensions = (9,9)

    def getDimensions():
        return dimensions

    def updateMap(self, x_position, y_position):
        #if valideMove ==true:
            map[character.get_x_position][character.get_y_position] = 0
            map[x_position][y_position] = 1

    def generateMap(self, x_position, y_position):
        self.map = [[0 for i in range(9)] for j in range(9)]
        self.map[x_position][y_position] = 1

    def getMap():
        return self.map
        
    def printMap(self):
        print("map size: " + str(len(self.map)))
        print(self.map)

    



    
