class Train:
    def __init__(self):
        self.__TotalSeats=20
        self.Seats=[['W','M','M','W'],['W','M','M','W'],['W','M','M','W'],['W','M','M','W'],['W','M','M','W']]
        
    def SeatsAwailable(self):
        count=0
        for i in self.Seats:
            for a in i:
                if a!='B':
                    count+=1
        return count
    def BookSeat(self,Option):
        a=self.Seats
        for i in range(0,len(a)):
            for j in range (0,len(a[0])):
                
                if a[i][j] == Option and a[i][j]!='B':
                    a[i][j]= 'B'
                    self.Seats=a
                    
                    return [i,j]
        return "No Seates are awailable for your selected option"
    
    def CancelSeat(self,SeatID):
        a,b=SeatID
        c=self.Seats
        if c[a][b]!='B':
            return "Entered Wrong SeatID"
        digit= a*10+b
        if digit%10==0 or digit%10==3:
            c[a][b]='W'
            self.Seats=c
            print(self.Seats)
            return "the seat has been canceled"
        
        c[a][b]='M'
        self.Seats=c
        return  "the seat has been canceled"
        
        
        
    def SeatPositions(self):
       return self.Seats
               