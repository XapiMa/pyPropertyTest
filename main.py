
class Test:
    def __init__(self):
        self.__get_only = "get_only"
        self.__set_only = "set_only"
        self.__get_and_set = "get_and_set"
    
    @property
    def get_only(self):
        return self.__get_only
    @property
    def get_and_set(self):
        return self.__get_and_set
    @get_and_set.setter
    def get_and_set(self, get_and_set):
        self.__get_and_set = get_and_set



if __name__ == "__main__":
    test = Test()

    try:
        _ = test.set_only
        print("set_only CAN be referenced")
    except AttributeError:
        print("set_only CAN NOT be referenced")
    try:
        test.set_only = "set_only changed"
        print("set_only CAN set the value")
    except AttributeError:
        print("set_only CAN NOT set the value")

    try:
        _ = test.get_only
        print("get_only CAN be referenced")
    except AttributeError:
        print("get_only CAN NOT be referenced")
    try:
        test.get_only = "get_only changed"
        print("get_only CAN set the value")
    except AttributeError:
        print("get_only CAN NOT set the value")

    try:
        _ = test.get_and_set
        print("get_and_set CAN be referenced")
    except AttributeError:
        print("get_and_set CAN NOT be referenced")
    try:
        test.get_and_set = "get_and_set changed"
        print("get_and_set CAN set the value")
    except AttributeError:
        print("get_and_set CAN NOT set the value")
    test.get_and_set = "get_and_set changed"
    

