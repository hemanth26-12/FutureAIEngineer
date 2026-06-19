class Student:
    def show_name(self,name):
        self.__name = name
        print("Student Name:",self.__name)


s1 = Student()
s1.show_name("Hemanth")
