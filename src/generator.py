import random

class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.centerX = x + width / 2
        self.centerY = y + height / 2
        self.connections = []
    
    def getCenterX(self):
        return self.centerX

    def getCenterY(self):
        return self.centerY

    def findXDist(self, other):
        return abs(self.centerX - other.getCenterX)

    def findYDist(self, other):
        return abs(self.centerY - other.getCenterY)

    def addConnection(self, other):
        self.connections.append(other)
    
    def getNumConnections(self):
        return len(self.connections)

    def getConnections(self):
        return self.connections
class DungeonMap:
    
    def __init__(self):
        self.max_dun_width = 100
        self.max_dun_height = 100
        self.min_dun_width = 100
        self.min_dun_height = 100

        self.max_num_rooms = 10
        self.min_num_rooms = 5
        self.min_dist_from_end = 5
        self.min_connections = 2
        self.max_connections = 4

        self.max_room_width = 20
        self.max_room_height = 20
        self.min_room_width = 5
        self.min_room_height = 5
        self.map = [ [ 0 for i in range(0, self.max_dun_width) ] for j in range(0, self.max_dun_height)]
        self.roomList = []

    def createRooms(self):
        num_rooms = random.randint(self.min_num_rooms, self.max_num_rooms + 1)
        for i in range(0, num_rooms):
            x = random.randint(0, self.max_dun_width)
            y = random.randint(0, self.max_dun_height)
            tempHeight = random.randint(self.min_room_height, self.max_room_height)
            tempWidth = random.randint(self.min_room_width, self.max_room_width)
            self.roomList.append(Room(x, y, tempWidth, tempHeight))
            self.__drawRect(x, y, tempHeight, tempWidth)
        self.__connectAdjRooms()

    def __drawRect(self, x, y, rectHeight, rectWidth):
        if x - self.min_dist_from_end < 0:
            temp = abs(x - self.min_dist_from_end)
            x += temp
        elif x + self.min_dist_from_end >= self.max_dun_width:
            temp = x + self.min_dist_from_end - self.max_dun_width
            x -= temp
        if y - self.min_dist_from_end < 0:
            temp = abs(y - self.min_dist_from_end)
            y += temp
        elif y + self.min_dist_from_end >= self.max_dun_height:
            temp = y + self.min_dist_from_end - self.min_dun_height
            y -= temp
        for row in range(y, rectHeight + y):
            for col in range(x, rectWidth + x):
                if row == y or row == (rectHeight + y - 1) or col == x or col == (rectWidth + x - 1) or row == self.max_dun_height - 1 or col == self.max_dun_width - 1:
                    self.__drawPoint(col, row, 2)
                else:
                    self.__drawPoint(col, row, 1)

    def __drawPoint(self, x, y, type):
        if (x >= 0 and x < self.max_dun_width) and (y >=0 and y < self.max_dun_height):
            self.map[x][y] = type

    def __connectAdjRooms(self):
        for row in range(0, self.max_dun_height):
            for col in range(0, self.max_dun_width):
                if row == 0 or col == 0 or row == self.max_dun_height - 1 or col == self.max_dun_width - 1:
                    continue
                if self.map[col - 1][row] == 1 and self.map[col + 1][row] == 1:
                    self.map[col][row] = 1
                elif self.map[col][row + 1] == 1 and self.map[col][row - 1] == 1:
                    self.map[col][row] = 1
        
        for row in range(0, self.max_dun_height):
            for col in range(0, self.max_dun_width):
                if row <= 1 or col <= 1 or row >= self.max_dun_height - 2 or col >= self.max_dun_width - 2:
                    continue
                if self.map[col - 2][row] == 1 and self.map[col + 1][row] == 1:
                    self.map[col][row] = 1
                    self.map[col - 1][row] = 1
                elif self.map[col][row + 2] == 1 and self.map[col][row - 1] == 1:
                    self.map[col][row] = 1
                    self.map[col][row + 1] = 1
    
    def printMap(self):
        for row in range(0, self.max_dun_height):
            for col in range(0, self.max_dun_width):
                print(self.map[col][row], end='')
            print()

    # def __createConnections(self):
    #     for room in self.roomList:
    #         tmp_connections = random.randint(self.min_connections, self.max_connections + 1)
    #         while room.getNumConnections() < tmp_connections:
    #             temp = self.__randomRoom(room)
    #             room.addConnection(temp)
    #             temp.addConnection(room)


    
    # def __createVConnection(self):
    #     return

    # def __createHConnection(self):
    #     return

    # def __randomRoom(self, room):
    #     temp = 0
    #     while room == self.roomList[temp] and self.roomList[temp] in room.getConnections():
    #         temp = random.randint(0, len(self.roomList))
    #     return temp

            
def main():
    dungeon = DungeonMap()
    dungeon.createRooms()
    dungeon.printMap()

main()