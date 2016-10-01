class Person:
    #class attributes
    #directly accessible without creating an instance of the class
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')
    
    def __init__(self, title, name, surname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)
        self.title = title
        self.name = name
        self.surname = surname
        print(self.title)

person=Person("Dr","KAMAL","AGRAWAL")


class stat:
    #used to provide default attribute values
    #class objects are immutable otherwise ot wud have affected all the other objects too..
    x=1
    def __init__(self):
        self.x=self.x+1
        print(self.x)

st1=stat()  # 2
st2=stat()  # 2
