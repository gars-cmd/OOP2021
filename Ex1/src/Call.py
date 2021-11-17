class Call:
    INIT = 0
    GOING2SRC = 1
    GOING2DEST = 2 
    DONE = 3
    UP =1
    DOWN =-1
    pos:int
    state = INIT
    allocated:int

    def __init__(self, time:float , src:int , dest:int , allocated:int):
        self.time = time
        self.src = src
        self.dest = dest
        self.allocated = 0

    def getState(self)->int:
        return self.state
    
    def getTime(self)->float:
        return self.time

    def getType(self)->int:
        if int(self.src)<int(self.dest):
            return self.UP
        else:
            return self.DOWN
    
    def allocatedTo(self):
        return self.allocated
        
    def toString(self):
        print(self.time , self.src , self.dest)
        
    def getSrc(self)->int:
        return self.src
    
    def getDest(self)->int:
        return self.dest
    
    def setAllocate(self , x:int):
        self.allocated = x
        