class Student:

    def __init__(self, frist_name, last_name, matric) -> None:
        self._frist_name = frist_name
        self._last_name = last_name
        self._matric = matric

    @property
    def frist_name(self):
        return self._frist_name
    
    @frist_name.setter
    def frist_name(self, value):
        print(self._frist_name, "change frist name to ->", value)
        self._frist_name = value

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        print(self._last_name, "change last name to ->", value)
        self._last_name = value

    @property
    def matric(self):
        return self._matric

if __name__ == "__main__":
    mrA = Student("MR.A", "Penny", "66104781")
    print("I'm", mrA.frist_name, mrA.last_name, "code :", mrA.matric)
    mrA.frist_name = "Mr.Adobe"
    mrA.last_name = "Catch"
    # mrA.matric = "111111" <- We can't update mrA.matric
    print("Update ->", mrA.frist_name, mrA.last_name, "code :", mrA.matric)


