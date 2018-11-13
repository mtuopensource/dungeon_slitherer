import random
import math
from config_reader import readConfig

class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.centerX = x + int(width / 2)
        self.centerY = y + int(height / 2)
        self.connections = []
    
    def getCenterX(self):
        return self.centerX

    def getCenterY(self):
        return self.centerY

    def findXDist(self, other):
        return abs(self.centerX - other.getCenterX())

    def findYDist(self, other):
        return abs(self.centerY - other.getCenterY())

    def addConnection(self, other):
        self.connections.append(other)
    
    def getNumConnections(self):
        return len(self.connections)

    def getConnections(self):
        return self.connections
class DungeonMap:
    
    def __init__(self):
        config = readConfig("../configs/dungeon_generation.json")
        self.max_dun_width = config["max_dun_width"]
        self.max_dun_height = config["max_dun_height"]
        self.min_dun_width = config["min_dun_width"]
        self.min_dun_height = config["min_dun_height"]

        self.max_num_rooms = config["max_num_rooms"]
        self.min_num_rooms = config["min_num_rooms"]
        self.min_dist_from_end = config["min_dist_from_end"]
        self.min_connections = config["min_connections"]
        self.max_connections = config["max_connections"]

        self.max_room_width = config["max_room_width"]
        self.max_room_height = config["max_room_height"]
        self.min_room_width = config["min_room_width"]
        self.min_room_height = config["min_room_height"]
        self.map = [ [ ' ' for i in range(0, self.max_dun_width) ] for j in range(0, self.max_dun_height)]
        self.roomList = []
        self.actual_height = random.randint(self.min_dun_height, self.max_dun_height + 1)
        self.actual_width = random.randint(self.min_dun_width, self.max_dun_width + 1)


    def createRooms(self):
        num_rooms = random.randint(self.min_num_rooms, self.max_num_rooms)
        for i in range(0, num_rooms):
            x = random.randint(0, self.actual_width)
            y = random.randint(0, self.actual_height)
            tempHeight = random.randint(self.min_room_height, self.max_room_height)
            tempWidth = random.randint(self.min_room_width, self.max_room_width)
            self.roomList.append(Room(x, y, tempWidth, tempHeight))
            self.__drawRect(x, y, tempHeight, tempWidth)
        self.__createConnections()

    def __drawRect(self, x, y, rectHeight, rectWidth):
        if x - self.min_dist_from_end < 0:
            temp = abs(x - self.min_dist_from_end)
            x += temp
        elif x + self.min_dist_from_end >= self.actual_width:
            temp = x + self.min_dist_from_end - self.actual_width
            x -= temp
        if y - self.min_dist_from_end < 0:
            temp = abs(y - self.min_dist_from_end)
            y += temp
        elif y + self.min_dist_from_end >= self.actual_height:
            temp = y + self.min_dist_from_end - self.actual_height
            y -= temp
        for row in range(y, rectHeight + y):
            for col in range(x, rectWidth + x):
                self.__drawPoint(col, row, '1')

    def __drawPoint(self, x, y, type):
        if (x >= 0 and x < self.actual_width) and (y >=0 and y < self.actual_height):
            self.map[x][y] = type

    # def __connectAdjRooms(self):
    #     for row in range(0, self.max_dun_height):
    #         for col in range(0, self.max_dun_width):
    #             if row == 0 or col == 0 or row == self.max_dun_height - 1 or col == self.max_dun_width - 1:
    #                 continue
    #             if self.map[col - 1][row] == 1 and self.map[col + 1][row] == 1:
    #                 self.map[col][row] = 1
    #             elif self.map[col][row + 1] == 1 and self.map[col][row - 1] == 1:
    #                 self.map[col][row] = 1
        
    #     for row in range(0, self.max_dun_height):
    #         for col in range(0, self.max_dun_width):
    #             if row <= 1 or col <= 1 or row >= self.max_dun_height - 2 or col >= self.max_dun_width - 2:
    #                 continue
    #             if self.map[col - 2][row] == 1 and self.map[col + 1][row] == 1:
    #                 self.map[col][row] = 1
    #                 self.map[col - 1][row] = 1
    #             elif self.map[col][row + 2] == 1 and self.map[col][row - 1] == 1:
    #                 self.map[col][row] = 1
    #                 self.map[col][row + 1] = 1
    
    def printMap(self):
        for row in range(0, self.actual_height):
            for col in range(0, self.actual_width):
                print(self.map[col][row], end='')
            print()

    def __createConnections(self):
        for room in self.roomList:
            tmp_connections = random.randint(self.min_connections, self.max_connections + 1)
            while room.getNumConnections() < tmp_connections:
                temp = self.__randomRoom(room)
                room.addConnection(self.roomList[temp])
                self.roomList[temp].addConnection(room)

        for room in self.roomList:
            for conn in room.getConnections():
                self.__createPath(room, conn)
    
    def __createPath(self, room_one, room_two):
        x_one = room_one.getCenterX()
        y_one = room_one.getCenterY()
        x_two = room_two.getCenterX()
        y_two = room_two.getCenterY()

        strt_x = self.__findMin(x_one, x_two)
        strt_y = 0
        dest_x = 0
        dest_y = 0

        if strt_x == x_one:
            strt_y = y_one
            dest_x = x_two
            dest_y = y_two
        else:
            strt_y = y_two
            dest_x = x_one
            dest_y = y_one

        row = strt_y
        col = strt_x
        while True:
            curr_dist = self.__distance(col, row, dest_x, dest_y)
            if curr_dist == 0:
                break
            if self.__distance(col, row - 1, dest_x, dest_y) < curr_dist:
                self.__drawPoint(col, row - 1, '1')
                row -= 1
                continue
            elif self.__distance(col, row + 1, dest_x, dest_y) < curr_dist:
                self.__drawPoint(col, row + 1, '1')
                row += 1
                continue
            elif self.__distance(col - 1, row, dest_x, dest_y) < curr_dist:
                self.__drawPoint(col - 1, row, '1')
                col -= 1
                continue
            elif self.__distance(col + 1, row, dest_x, dest_y) < curr_dist:
                self.__drawPoint(col + 1, row, '1')
                col += 1
                continue
            

    def __distance(self, a, b, x, y):
        return math.sqrt((a - x)**2 + (b - y)**2)

    def __findMin(self, x, y):
        if (x < y):
            return x
        return y

    def __randomRoom(self, room):
        temp = 0
        while True:
            temp = random.randint(0, len(self.roomList) - 1)
            if not (room == self.roomList[temp] and self.roomList[temp] in room.getConnections()):
                break
        return temp
    
    def getMap(self):
        return self.map

            
def main():
    dungeon = DungeonMap()
    dungeon.createRooms()
    dungeon.printMap()
main()