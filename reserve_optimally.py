import operator
from Input_processing import Input

class SeatReserve:
    def __init__(self, movie_thtr):
        self.movie_thtr = movie_thtr
        self.rowSeatsCount = [self.movie_thtr.getTheatresize()[1]]*self.movie_thtr.getTheatresize()[0]
        self.row_count = self.movie_thtr.getTheatresize()[1]

    def seat_req(self, req_list):
        req_list = sorted(req_list, key=operator.itemgetter(1), reverse=True)
        for i in req_list:
            req_no, no_of_seats = i[0], i[1]
            self.bookSeats(no_of_seats,req_no)

    def bookSeats(self, no_of_seats, req_no):
        row_seats = self.empty_row()
        self.divided_booking(row_seats, no_of_seats, req_no)
        #print(self.movie_thtr.getArrangement())

    def aisle(self, no_of_seats):
        for i in range(len(self.rowSeatsCount)):
            if self.rowSeatsCount[i] >= no_of_seats:
                return i
        dec_rowSeatsCount = []
        for i in range(len(self.rowSeatsCount)):
            dec_rowSeatsCount.append([self.rowSeatsCount[i],i])
        dec_rowSeatsCount = sorted(dec_rowSeatsCount, key=operator.itemgetter(0), reverse=True)
        count, i, multiple_aisle = 0, 0, []
        while(count < no_of_seats):
            count += dec_rowSeatsCount[i][0]
            multiple_aisle.append(dec_rowSeatsCount[i])
            i += 1
        return multiple_aisle

    def no_together_seats(self, no_of_seats, req_no):
        aisle_no = self.aisle(no_of_seats)
        if type(aisle_no) == list:
            for i in aisle_no:
                if no_of_seats >= i[0]:
                    seats_aisle = i[0]
                    self.bookSeats_aisle(seats_aisle, req_no)
                    no_of_seats -=  seats_aisle
                elif no_of_seats <= i[0]:
                    seats_aisle = i[0] - no_of_seats
                    self.bookSeats_aisle(seats_aisle, req_no)
                    no_of_seats -=  seats_aisle
        else:
            self.bookSeats_aisle(no_of_seats, req_no)

    def seat(self, aisle):
        for i in range(self.row_count):
            if self.movie_thtr.getSeatAvailability(aisle, i) == None:
                return i

    def bookSeats_aisle(self, no_of_seats, req_no):
        aisle_no = self.aisle(no_of_seats)
        start_book = self.seat(aisle_no)
        while (no_of_seats > 0):
            self.movie_thtr.setSeatAsReserved(aisle_no, start_book, req_no)
            start_book += 1
            no_of_seats -= 1
            self.rowSeatsCount[aisle_no] -= 1

    def empty_row(self):
        empty_row = []
        for i in range(len(self.rowSeatsCount)):
            if self.rowSeatsCount[i] == self.row_count:
                empty_row.append(self.rowSeatsCount[i])
        return empty_row

    def divided_booking(self, row_seats, no_of_seats, req_no):
        if len(row_seats) > 0:
            for i in row_seats:
                if no_of_seats > i:
                    self.bookSeats_aisle(i, req_no)
                    no_of_seats -= i
                elif no_of_seats < i:
                    self.bookSeats_aisle(no_of_seats, req_no)
                    no_of_seats = i - no_of_seats
                    break
                elif no_of_seats == i:
                     self.bookSeats_aisle(no_of_seats, req_no)
                     no_of_seats = no_of_seats - i
                     break
        if (not row_seats):
            self.no_together_seats(no_of_seats, req_no)

    def CustIndexseatedTogether(self, name, seatings):
        import numpy as np
        arr = np.array(seatings)
        a = arr.flatten()
        count = 1
        seperator = []
        for i in range(len(a) - 1):
            if (a[i] == name and a[i] == a[i + 1]):
                count = count + 1
            elif (a[i] == name):
                seperator.append(count)
                count = 1
        if (a[i + 1] == name):
            seperator.append(count)
            count = 1
        mul = 1
        for i in seperator:
            mul = mul * (i / sum(seperator))
        return mul

    def bestSeatvalue(self, name, seatings):
        totalRow = len(seatings)
        col = len(seatings[0])
        middle = (col + 1) // 2
        count = 0
        summation = 0
        for i in range(len(seatings)):
            for j in range(len(seatings[i])):
                if seatings[i][j] == name:
                    if j <= middle:
                        val = ((totalRow - i) / totalRow) * ((j + 1) / middle)
                    else:
                        val = ((totalRow - i) / totalRow) * (((j + 1) - middle) / middle)
                    summation = summation + val
                    count = count + 1
        customer_satisfaction = summation / count
        return customer_satisfaction

    def customerIndex(self, validReq):
        seatAr = self.movie_thtr.getArrangement()
        for i in validReq:
            customer_satisfaction = self.CustIndexseatedTogether(i[0], seatAr) * self.bestSeatvalue(i[0], seatAr)



