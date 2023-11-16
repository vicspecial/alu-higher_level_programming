#!/usr/bin/python3
class Square:
    """
    A class to represent a square.

    ...

    Attributes
    ----------
    size : int
        size of the square

    Methods
    -------
    area(self)
        Returns the area of the square.
    """

    def init(self, size=0):
        """
        Constructs all the necessary attributes for the Square object.

        Parameters
        ----------
        size : int, optional
            The size of the square (default is 0)

        Raises
        ------
        TypeError
            If size is not an integer
        ValueError
            If size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns
        -------
        int
            The area of the square (size * size)
        """

        return self.__size ** 2
`
