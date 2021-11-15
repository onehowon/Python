import math

def LocalSeatInput():
    A_localSeat = int(input("A지역구 의석 수 입력 \n"))
    B_localSeat = int(input("B지역구 의석 수 입력 \n"))
    C_localSeat = int(input("C지역구 의석 수 입력 \n"))
    D_localSeat = 253 - (A_localSeat + B_localSeat + C_localSeat )
    print("D 지역구 의석 은 자동계산에 의해 %d 입니다" %D_localSeat)

    return A_localSeat,B_localSeat,C_localSeat,D_localSeat

def PartyApprovalRatingInput():
    A_rating = float(input("A 정당 지지율 입력(합계 100프로) \n"))
    B_rating = float(input("B 정당 지지율 입력(합계 100프로) \n"))
    C_rating = float(input("C 정당 지지율 입력(합계 100프로) \n"))
    D_rating = 100 - (A_rating + B_rating + C_rating)
    print("D 정당 지지율은 자동계산에 의해 %f 입니다" %D_rating)

    return A_rating,B_rating,C_rating,D_rating


def GetSemiLinkedSeat(localSeat,rate):
    TotalSeat = 300
    Semi_linked_seat = math.floor(((TotalSeat * (rate/100)) - localSeat) / 2)
    if Semi_linked_seat <0:
        Semi_linked_seat = 0
    
    return Semi_linked_seat
    

def GetParallel_Seat(rate):
    TotalParallelSeat = 17
    Parallel_Seat = round(TotalParallelSeat * (rate /100))
    if Parallel_Seat<0:
        Parallel_Seat = 0

    return Parallel_Seat
    
                     

A_LocalSeat,B_LocalSeat,C_LocalSeat,D_LocalSeat = LocalSeatInput()
A_Rating,B_Rating,C_Rating,D_Rating = PartyApprovalRatingInput()

LocalSeat = [A_LocalSeat, B_LocalSeat, C_LocalSeat, D_LocalSeat]
Rating = [A_Rating,B_Rating,C_Rating,D_Rating]
Semi_linked_seats = []
Parallel_Seats = []
Seats = []

for i in range(4):
    Semi_linked_seats.append(GetSemiLinkedSeat(LocalSeat[i],Rating[i]))

sum_Semi_linked_seats = Semi_linked_seats[0] + Semi_linked_seats[1] + Semi_linked_seats[2] + Semi_linked_seats[3]

for i in range(4):
    Semi_linked_seats[i] = round(Semi_linked_seats[i] / sum_Semi_linked_seats * 30)


for i in range(4):
    Parallel_Seats.append(GetParallel_Seat(Rating[i]))
    Seats.append(LocalSeat[i] + Semi_linked_seats[i] + Parallel_Seats[i])



print("A좌석 수: %d\n" %Seats[0])
print("B좌석 수: %d\n" %Seats[1])
print("C좌석 수: %d\n" %Seats[2])
print("D좌석 수: %d\n" %Seats[3])
