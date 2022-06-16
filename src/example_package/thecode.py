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

    def a_public_function(self) -> bool:
        """Does some action and can be publically called

        Returns:
            bool: always return True
        """
        return True
    
    def another_function(self, arg1:int) -> int:
        """Another function that multiplies by 2

        Args:
            arg1 (int): Input value

        Returns:
            int: arg1 * 2
        """
        return arg1 * 2

    def function3(self, arg1: int) -> int:
        """_summary_

        :param arg1: _description_
        :type arg1: int
        :return: _description_
        :rtype: int
        """
        return arg1 * 3
