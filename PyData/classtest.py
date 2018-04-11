class Tester:
    testobj = "non_instantiated"

    def __init__(self):
        self.initialized = "instantiated"

    @classmethod
    def printclass(cls):
        #print(cls(testobj))
        print(cls(initialized))

    @staticmethod
    def printstatic():
        print(testobj)
        print(self.initialized)


if __name__=="__main__":
    test=Tester()
    print(Tester().testobj)
    Tester().printclass()
