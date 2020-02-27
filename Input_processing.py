import os
import operator
import pandas as pd

class Input:
    def __init__(self, fileName, movie_thtr):
        self.fileName = fileName
        self.movie_thtr = movie_thtr
        self.totalSize = self.movie_thtr.getTheatresize()[0] * self.movie_thtr.getTheatresize()[1]

    def processInput(self, file):
        try:
            seat_req = pd.read_csv(file, sep=' ', header=None)
            seat_req = [list(i) for i in seat_req.values]
            return seat_req
        except FileNotFoundError:
            print("File Not Found")
            return
        except pd.errors.EmptyDataError:
            print("Empty File")
            return
        except:
            print("Error in retrieval")
            return

    def getValidreqlist(self, req_list):
        seats_sum, invalid_req, i = 0, [], 0
        while True:
            try:
                if (i >= len(req_list)): break
                req_list[i][1] = int(req_list[i][1])
                if (req_list[i][1]<=0) or (req_list[i][0][0] != 'R'):
                    raise Exception
                int(req_list[i][0][1:])
            except Exception:
                del req_list[i]
                i -= 1
            i += 1
        for i in req_list:
            seats_sum += i[1]
        extra_seats = seats_sum - self.totalSize
        if extra_seats > 0:
            formatted_input = self.formatInput(req_list)
            values = formatted_input
            n = len(formatted_input)
            optimal_requests = self.findOptimalArrangement(self.totalSize, formatted_input, values, n)
            req_list = self.maptoReq(optimal_requests, req_list)
        return req_list

    def findOptimalArrangement(self, total_size, formatted_input, values, n):
        K = [[0 for x in range(total_size + 1)] for x in range(n + 1)]
        for i in range(n + 1):
            for w in range(total_size + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif formatted_input[i - 1] <= w:
                    K[i][w] = max(values[i - 1] + K[i - 1][w - formatted_input[i - 1]], K[i - 1][w])
                else:
                    K[i][w] = K[i - 1][w]
        res = K[n][total_size]
        w = total_size
        optimal_requests = []
        for i in range(n, 0, -1):
            if res <= 0:
                break
            if res == K[i - 1][w]:
                continue
            else:
                optimal_requests.append(formatted_input[i - 1])
                res = res - values[i - 1]
                w = w - formatted_input[i - 1]
        return optimal_requests
                
    def formatInput(self, req_list):
        req_list = sorted(req_list, key=operator.itemgetter(1))
        formatted_input = []
        for i in req_list:
            formatted_input.append(i[1])
        return formatted_input

    def maptoReq(self, optimal_requests, originalList):
        i = 0
        while(i<len(originalList)):
            if originalList[i][1] in optimal_requests:
                del optimal_requests[optimal_requests.index(originalList[i][1])]
            else:
                del originalList[i]
                continue
            i+=1
        return originalList



