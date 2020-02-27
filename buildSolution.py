from reserve_optimally import SeatReserve
from theatre import Theatre
from Input_processing import Input

class BuildSolution:
    def mainFunc(self, fileName, outputFile):
        MovieTheatre = Theatre('Cineplex', (10, 20))
        inputFile = Input(fileName, MovieTheatre)
        seatAllocate = SeatReserve(MovieTheatre)
        reservation_requests = inputFile.processInput(fileName)
        if not reservation_requests:
            return
        validReq = inputFile.getValidreqlist(reservation_requests)
        seatAllocate.seat_req(validReq)
        seatAllocate.customerIndex(validReq)
        return self.output_file(MovieTheatre.getArrangement(),validReq, outputFile)

    def output_file(self,allocatedSeats, reservation_requests, outputFile):
        allocated = {}
        for i in reservation_requests:
            allocated[i[0]] = []
        s = 64 + len(allocatedSeats)
        for i in allocatedSeats:
            for j in range(len(i)):
                if i[j] != None:
                    position = chr(s) + str(j + 1)
                    allocated[i[j]].append(position)
            s = s - 1
        alloc = []
        for key, value in allocated.items():
            alloc.append([key] + value)
        op = []
        for i in alloc:
            temp = ''
            for j in i:
                if temp: temp+=j+','
                else: temp+=j+' '
            op.append(temp[:-1])
        with open(outputFile , 'w') as fo:
            fo.writelines('%s\n' % i for i in op)
        return outputFile

