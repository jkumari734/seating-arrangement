class Theatre:
    def __init__(self, theatreName, size):
        self.theatreName = theatreName
        self.__size = size
        self.__arrangement = [[None for x in range(size[1])] for y in range(size[0])]

    def getTheatresize(self):
        return self.__size

    def getArrangement(self):
        return self.__arrangement

    def getSeatAvailability(self, m, n):
        return self.__arrangement[m][n]

    def setSeatAsReserved(self, m, n, req_no):
        self.__arrangement[m][n] = req_no
'''
    def setArrangement(self, new_arrangement):
        self.__arrangement = new_arrangement
'''