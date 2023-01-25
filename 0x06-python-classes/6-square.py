#!/usr/bin/python3


class Square:
    """A class that defines a square by size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the square class with optional size and position"""
        self.size = size
        self.position = position


    @property
    def size(self):
        """Method to retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    @property
    def position(self):
        """Method to retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Method to set the position of the square"""
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int
        or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        """Method to calculate the area of the square"""
        return self.__size * self.__size


    def my_print(self):
        """Method to print the square with the character #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")

            for i in range(self.__size):

                print(" " * self.__position[0], end="")

                print("#" * self.__size)
