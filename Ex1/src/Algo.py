
from Building import Building
from Call import Call
from Elevator import Elevator
import json
import csv
import sys

count0=0
count1=0



def jsonToBuilding(file):
    f= open(file)
    data = json.load(f)
    building =Building(minFloor=data["_minFloor"] , maxFloor=data["_maxFloor"] , elevators=data["_elevators"])
    f2 = data["_elevators"]
    list1 = []
    for item in f2:
         list1.append(Elevator(id=item["_id"] , speed=item["_speed"], minFloor=item["_minFloor"] , maxFloor =item["_maxFloor"] , closeTime=item["_closeTime"] , openTime=item["_openTime"] , startTime=item["_startTime"] ,stopTime=item["_stopTime"]))
    building.elevators = list1
    return building
    

def csvToCall(file):
    listCalls =[]
    try:  
        with open(file,'r') as f:
            calls = csv.reader(f)
            for row in calls:
                calld = Call(row[1],row[2],row[3] , 0)
                listCalls.append(calld)
    except:
        print("error in reading file")
    return listCalls        

# def allocateAnElevator(b:Building , c:Call):    #algorithm that allocated according to speed of the elevators
    
#     choosen=0
#     if Building.numOfElevators(b)==1:
#         return choosen
#     else:
#         Categories = Building.elevatorsCategories(b)
        
#         listOfSpeeder = Categories[0]
#         listOfSlower = Categories[1]

#         q = abs((b.minFloor-b.maxFloor)+1)/b.numOfElevators()
#         if abs(int(Call.getSrc(c))-int(Call.getDest(c))) > q*2:
#             global count0,count1
#             choosen = count0 % (len(listOfSpeeder)+1)
#             count0=count0+1
#         else:
#             choosen = count1 % (len(listOfSlower)+1)
#             count1 = count1 + 1
#     print(choosen)        
#     return choosen

def allocateAnElevator2(b:Building , c:Call):    
    choosen = 0
    rangeElev = Building.numOfElevators(b)
    if rangeElev==1:
        return choosen
    else:
        elevatorDown = []
        elevatorUp = []
        for elevator in range(rangeElev):
            if elevator<(rangeElev/2):
                elevatorUp.append(elevator)
                
            else:
                elevatorDown.append(elevator)
        global count0,count1
        if Call.getType(c)==1:
            choosen = elevatorUp[count0 % (len(elevatorUp))]
            count0=count0+1
        else:
            choosen= elevatorDown[count1 % (len(elevatorDown))]
            count1 = count1+1
    print(choosen)
    return choosen
            
    
def writeOnCsv(fileToWriteOn , listcall:list):
    with open (fileToWriteOn , 'w' , newline= '') as f:
        writer = csv.writer(f)
        for calls in listcall:
            writer.writerow(['Elevator call' , Call.getTime(calls) , Call.getSrc(calls) , Call.getDest(calls) ,-1 ,  Call.allocatedTo(calls)])
              
    

if __name__ == "__main__":
    fileBuild = sys.argv[1]
    fileCall = sys.argv[2]
    fileOut = sys.argv[3]

    b = jsonToBuilding(fileBuild)
    listCall = csvToCall(fileCall)   
     
    
    
    for item in listCall:
        Call.setAllocate(item,allocateAnElevator2(b,item))
       
    writeOnCsv('test.csv' , listCall)
        
         

        
