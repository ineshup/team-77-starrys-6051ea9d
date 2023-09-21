class character:

    name = ""

    current_x_position = 0
    current_y_position = 0
    
    currentPosition = (0,0)

    startingPosition = (0,0)



    def move(self,direction):

        if(direction == 'n'):
            self.currentPosition = (self.currentPositon[0], self.currentPosition[1]-1)
        if(direction =='e'):
            self.currentPosition = (self.currentPosition[0]+1, self.currentPosition[1])
        if(direction =='s'):
            self.currentPosition = (self.currentPosition[0], self.currentPosition[1]+1)
        if(direction=='w'):
            self.currentPosition = (self.currentPosition[0] - 1, self.currentPosition[1])
        

        

    def __init__(self, character_name):
        self.name = character_name

   
    def set_x_position(direction):

        if(direction=='n'):
            current_y_position = current_y_position+1
        if(direction == 'e'):
            current_x_position = current_x_position+1
        if(direction == 's'):
            current_y_position = current_y_position-1
        if(diretion == 'w'): 
            current_x_position = current_x_position-1


        
    def get_y_position(self):
        return self.current_y_position

    def get_x_position(self):
        return self.current_x_position
    def get_name(self):
        return self.name