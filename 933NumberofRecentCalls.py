class RecentCounter:

    def __init__(self):
        self.arr=[]
        
    def ping(self,t)->int:
        self.arr.append(t)
        if t <= 3000:
            return len(self.arr)
        
        for i in range(len(self.arr)):
            if self.arr[i]>=t-3000:
                return len(self.arr) - i

rc=RecentCounter()
print(rc.ping(1))
print(rc.ping(100))
print(rc.ping(3001))
print(rc.ping(3002))