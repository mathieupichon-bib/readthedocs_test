class AClass:
    def __init__(self, *args) -> None:
        for v in args:
            self.__dict__[v] = v

    def __repr__(self) -> str:
        rep = "AClass("
        for k, v in self.__dict__.items():
            rep += str(k) + "=" + str(v) + ","
        rep += ")"
        return rep
