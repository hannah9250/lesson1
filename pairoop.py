class Pairfinder:
    def __init__(self):
        self.data = (10,20,30,40,50,60,70)
    def findpair(self): 
        target = int(input("enter the target sum: "))
        found = False
        for i in range(len(self.data)): 
            for j in range(i + 1, len(self.data)): 
                if self.data[i]+self.data[j] == target: 
                    print("pairfound")
                    print("numbers: ", self.data[i], "and", self.data[j])
                    print("position: ", i ,"and", j)
                    found = True
        if not found: 
            print("no pair found")
t1 = Pairfinder()
t1.findpair()
        