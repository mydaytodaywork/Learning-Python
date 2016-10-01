class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def namef(self):
        print(self.name)
        #while modifying variables self must be used otherwise changes will not be reflected, try removing self in the below line and check the o/p
        self.name="kamal"
    def agef(self):
        print(self.age)

stud=student("Kamal",19)
stud.namef()
stud.namef()
stud.agef()
