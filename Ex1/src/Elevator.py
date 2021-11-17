class Elevator:
    UP=1
    LEVEL=0
    DOWN=-1
    ERROR =-2
    state=LEVEL
    pos=0

    def __init__(self , id:int , speed:float , minFloor:int , maxFloor:int , closeTime:float , openTime:float , startTime:float , stopTime:float):
        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.stopTime = stopTime
        self.startTime = startTime

    def getMinFoor(self)->int:
        return self.minFloor

    def getMaxFloor(self)->int:
        return self.maxFloor

    def getTimeForOpen(self)->float:
        return self.getTimeForOpen

    def getTimeForClose(self)->float:
        return self.getTimeForClose

    def getState(self)->int:
        return self.state

    def getPos(self)->int:
        return self.pos
    
    def goTo(self , destinationFloor:int)->bool:
        if self.state != self.LEVEL:
            print("the elevator is not resting")
            return False
        elif (destinationFloor<self.minFloor or destinationFloor>self.maxFloor):
            print("the destination floor is lower/bigger than the minimal floor/max floor")
            return False
        elif(destinationFloor == self.pos ):
            print("the elevator is already at the destination floor")
            return False
        else:
            self.pos = destinationFloor
            if destinationFloor<self.pos:
                self.state = self.DOWN
            else:
                self.state = self.UP
            return True
            

    def stop(self , stopFloor:int)->bool:
        if self.state==self.LEVEL:
            print("the elevator is already resting so he can't stop")
            return False
        elif (stopFloor<self.minFloor or stopFloor>self.maxFloor):
            print("the stop floor is lower/bigger than the minimal floor/max floor")
            return False
        elif(stopFloor == self.pos ):
            print("the elevator is already at the stop floor")
            return False
        else:
            self.pos = stopFloor
            self.state = self.LEVEL
            return True
    
    def getSpeed(self)->float:
        return self.speed

    def getSartTime(self)->float:
        return self.startTime
    
    def getStopTime(self)->float:
        return self.stopTime

    def getID(self)->int:
        return self.id
