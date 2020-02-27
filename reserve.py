import pandas as pd
import operator
from theatre import Theatre


class SeatReserve:

    def __init__(self, movie_thtr):
        self.movie_thtr = movie_thtr
        self.rowSeats_count = [self.movie_thtr.getTheatresize()[1]]*self.movie_thtr.getTheatresize()[0]
        self.row_count = self.movie_thtr.getTheatresize()[1]
        #print(self.seat_arrangement)

    def seat_req(self, req_list):
        for i in req_list:
            req_no = i[0]
            no_of_seats = i[1]
            self.bookSeats(no_of_seats,req_no)

    def bookSeats(self, no_of_seats, req_no):
        if no_of_seats < self.row_count:
            row_seats = self.empty_row(no_of_seats, req_no)
            self.divided_booking(row_seats, no_of_seats, req_no)
        elif no_of_seats > self.row_count:
            row_seats = self.empty_row(no_of_seats,req_no)
            self.divided_booking(row_seats, no_of_seats, req_no)
        #self.movie_thtr.setArrangement(self.seat_arrangement)
        print(self.movie_thtr.getArrangement())

# to get the pointer for empty seats (row wise)
    def aisle(self, no_of_seats):
        #print(self.rowSeats_count,"bacche hue seats")
        for i in range(len(self.rowSeats_count)):
            if self.rowSeats_count[i] >= no_of_seats:
                return i
        dec_rowSeats_count = []
        print('in')
        for i in range(len(self.rowSeats_count)):
            dec_rowSeats_count.append([self.rowSeats_count[i],i])
        dec_rowSeats_count = sorted(dec_rowSeats_count, key=operator.itemgetter(0), reverse=True)
        count = 0
        i = 0
        multiple_aisle = []
        while(count < no_of_seats):
            count = dec_rowSeats_count[i][0] + count
            multiple_aisle.append(dec_rowSeats_count[i])
            i = i +1
        return multiple_aisle


    def no_together_seats(self, no_of_seats, req_no):
        aisle_no = self.aisle(no_of_seats)
        print('aisle_no', aisle_no)
        for i in aisle_no:
            if no_of_seats >= i[0]:
                seats_aisle = i[0]
                self.bookSeats_aisle(seats_aisle, req_no)
                no_of_seats = no_of_seats - seats_aisle
            elif no_of_seats <= i[0]:
                seats_aisle = i[0] - no_of_seats
                self.bookSeats_aisle(seats_aisle, req_no)
                no_of_seats = no_of_seats - seats_aisle


# to get the pointer for empty seat (column wise)
    def seat(self, aisle):
        for i in range(self.row_count):
            if self.movie_thtr.getSeatAvailability(aisle, i) == None:
                return i

    def bookSeats_aisle(self, no_of_seats, req_no):
        aisle_no = self.aisle(no_of_seats)
        start_book = self.seat(aisle_no)
        order_post = []
        print(no_of_seats, 'no_of_seats')
        while (no_of_seats > 0):
            self.movie_thtr.setSeatAsReserved(aisle_no, start_book, req_no)
            start_book = start_book + 1
            no_of_seats = no_of_seats - 1
            self.rowSeats_count[aisle_no] -= 1
            order_post.append(str(aisle_no) + str(start_book))
        return order_post

    def empty_row(self, no_of_seats, req_no):
        empty_row = []
        for i in range(len(self.rowSeats_count)):
            if self.rowSeats_count[i] == self.row_count:
                empty_row.append(self.rowSeats_count[i])
        return empty_row

    def divided_booking(self, row_seats, no_of_seats, req_no):
        if len(row_seats) > 0:
            for i in row_seats:
                if no_of_seats > i:
                    seats_aisle = i
                    #print('seats_aisle', seats_aisle)
                    self.bookSeats_aisle(seats_aisle, req_no)
                    no_of_seats = no_of_seats - seats_aisle
                elif no_of_seats < i:
                    seats_aisle = no_of_seats
                    #print('seats_aisle when less',seats_aisle)
                    self.bookSeats_aisle(seats_aisle, req_no)
                    no_of_seats = i - seats_aisle
                    break
        if (not row_seats):
            self.no_together_seats(no_of_seats, req_no)


