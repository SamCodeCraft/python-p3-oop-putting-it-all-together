#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Initialize the internal size attribute
        self.size = size  # Use the property setter to validate the initial value
        self.condition = "Old"  # Initialize the condition attribute
    
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"