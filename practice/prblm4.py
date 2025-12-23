class Count:
    val = 0
    def __init__(self):
        Count.val += 1
    @classmethod
    def show(cls):
        print(cls.val)
obj1 = Count()
obj2 = Count()
obj3 = Count()
obj4 = Count()
Count.show()