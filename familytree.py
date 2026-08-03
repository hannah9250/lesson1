class Family: 
    def __init__(self, familyname, eyecolor):
        self.familyname = familyname
        self.eyecolor = eyecolor
    def showtraits(self): 
        print("family name: ", self.familyname)
        print("eye color: ", self.eyecolor)
class Child(Family): 
    def __init__(self, familyname, eyecolor, childname, hobby):
        super().__init__(familyname, eyecolor)
        self.childname = childname
        self.hobby = hobby
    def showtraits(self): 
        super().showtraits()
        print("child name: ", self.childname)
        print("hobby: ", self.hobby)
c = Child("potter", "blue", "harry", "magic")
c.showtraits()
print(issubclass(Child, Family))


        